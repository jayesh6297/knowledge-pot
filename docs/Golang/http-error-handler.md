# HTTP Error Handling in golang

Golang have excellent http library built in but it does not offer returning error for convient use case. 
where other router like echo does offer error returing handler. now in this post we are going to look at creating http error returning handler.
how create how to execute it.

## Creating custom http handler

What is http handler in go or rather what is `http.HandlerFunc` is?
In simple term http.HandlerFunc is whatever that implements `ServeHTTP(w http.ResponseWriter, r *http.Request)`.
See subsequent snippet to follow how we are creating custom handler which returns error.

```go linenums="1"
package main

import (
    "http"
    "errors"
)

type HandlerFunc func(w http.ResponseWriter, r *http.Request) error

func (h HandlerFunc) ServeHTTP(w http.ResponseWriter, r *http.Request) {
	if err := h(w, r); err != nil {
        http.Error(w, err.Error(), http.StatusInternalServerError)	    	
		return
	}
}

func main() {
    mux := http.NewServeMux()
    mux.Handle("/", HandlerFunc(func(w http.ResponseWriter, r *http.Request) error {
        return errors.New("this is error")
    }))
    http.ListenAndServe(":3000", mux)
}
```

- On line number 11 we implmented ServeHTTP method on our handler function
- Line number 12 executes our incoming handler and reurns any error from it
- On line 19 we converted `http.HandlerFunc` to our custom `HandlerFunc`

notice that this type of error handling now we can't specifiy status code and serve http will always return 500 as status.
we will look at how to tackle it in next section.

## Creating custom error for better response
- Basic idea here is we will create struct that implments both error and Marshler interfaces. 
- We need to implement Marsheler as golang doesn't know how to json encode errors
- Notice in MarshalJSON method we are returning custom struct with all field exported to encode json.

```go linenums="1"
type AppErr struct {
	err    error
	msg    string
	status int
}

func HTTPError(e error, m string, code int) AppErr {
	return AppErr{e, m, code}
}

// Method Unwrap tells go to extract exact error
// from bunch of other fields
func (e AppErr) Unwrap() error {
	return e.err
}

// Method Error implments error interface
func (e AppErr) Error() string {
	return e.err.Error()
}

// Method MarshalJson implements Marshaler interface
func (e AppErr) MarshalJSON() ([]byte, error) {
	return json.Marshal(struct {
		Err        string `json:"err,omitempty"`
		Msg        string `json:"msg,omitempty"`
		StatusCode int    `json:"status_code,omitempty"`
	}{
		e.Error(), e.msg, e.status,
	})
}
```

## Changing our ServeHTTP to handle custom error

```go linenums="1"
type HandlerFunc func(w http.ResponseWriter, r *http.Request) error

func (h HandlerFunc) ServeHTTP(w http.ResponseWriter, r *http.Request) {
	if err := h(w, r); err != nil {
		if errors.As(err, &AppErr{}) {
			e := err.(AppErr)
            w.Header().Set("Content-Type", "application/json")
			w.WriteHeader(e.status)
            if err := json.NewEncode(r).Encode(e); err != nil {
                log.Println(err)
            }
		}
		return
	}
}
```

## Complete Code

```go linenums="1"
package main

import (
	"encoding/json"
	"errors"
	"fmt"
	"net/http"
)

// JSON is repsonse helper functions
func JSON(w http.ResponseWriter, code int, payload any, headers map[string]string) error {
	for k, v := range headers {
		w.Header().Set(k, v)
	}
	w.WriteHeader(code)
	return json.NewEncoder(w).Encode(payload)
}

// Bind binds the request body to given model
func Bind[M any](r *http.Request) (M, error) {
	var m M
	return m, json.NewDecoder(r.Body).Decode(&m)
}

// Custom Handler func that Defines error on top of http.HandlerFunc
type HandlerFunc func(w http.ResponseWriter, r *http.Request) error

func (h HandlerFunc) ServeHTTP(w http.ResponseWriter, r *http.Request) {
	if err := h(w, r); err != nil {
		if errors.As(err, &AppErr{}) {
			e := err.(AppErr)
			fmt.Println(err)
			JSON(w, e.status, e, map[string]string{"Content-Type": "application/json"})
		}
		return
	}
}

// app err which implments custom
// JsonMarshaler and Error interface
type AppErr struct {
	err    error
	msg    string
	status int
}

func HTTPError(e error, m string, code int) AppErr {
	return AppErr{e, m, code}
}

func (e AppErr) Unwrap() error {
	return e.err
}

func (e AppErr) Error() string {
	return e.err.Error()
}

func (e AppErr) MarshalJSON() ([]byte, error) {
	return json.Marshal(struct {
		Err        string `json:"err,omitempty"`
		Msg        string `json:"msg,omitempty"`
		StatusCode int    `json:"status_code,omitempty"`
	}{
		e.Error(), e.msg, e.status,
	})
}

// api struct
type API struct {
	router *http.ServeMux
}

func (api *API) GetE(w http.ResponseWriter, r *http.Request) error {
	return HTTPError(errors.New("this is error"), "just error", 400)
}

func (api *API) ServeHTTP(w http.ResponseWriter, r *http.Request) {
	api.router.ServeHTTP(w, r)
}

func (api *API) Routes() {
	api.router.Handle("/", HandlerFunc(api.GetE))
}

func main() {
	mux := http.NewServeMux()
	api := &API{mux}
	api.Routes()
	srv := &http.Server{
		Addr:    ":8080",
		Handler: api,
	}
	srv.ListenAndServe()
}
```
