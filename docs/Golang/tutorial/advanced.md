---
tags:
    - golang
    - advanced
    - guides
---

### Time
---
- go has std lib package time which use to handle date and time.
- to format time string you can use time.Format("") and mention format of string like below &rarr;
```go linenums="1"
// Day of the month: "2" "_2" "02" 
// Day of the week: "Mon" "Monday"
// Month: "Jan" "January" "01" "1"
// Year: "2006" "06"
// Day of the year: "__2" "002"
// Hour: "15" "3" "03" (PM or AM)
// Minute: "4" "04"
// Second: "5" "05"
// AM/PM mark: "PM"
fmt.Println(time.Now().Format("2006 Jan 02 03:04 PM"))

// output
// 2022 Aug 22 01:43 PM
```
- parsing the datetime string into object
```go linenums="1"
// converting time string to Time object
parsedTime, err := time.Parse("02/01/2006 15:04", "06/02/1997 09:15")
if err != nil {
	fmt.Println(err)
}
fmt.Println(parsedTime.Format("02 Jan 2006 09:15PM"))
//output
// 06 Feb 1997 09:09AM
```

