---
tags:
    - golang
    - ide
    - neovim
    - lsp
---

This is the complete tutorial to configure neovim to work with golang and some other language as IDE.
we will explore some options and how neovim plugin system works as well lsp client and mason for installing our dependencies. 
If you are really new to vim/neovim ecosystem I recommend you to get familier with neovim using `:Tutor`
and you can also refer to awesome [nvim kickstarter](https://github.com/nvim-lua/kickstart.nvim).

# How to proceed with configuration

### Folder structure
- Neovim looks for init.lua file in config dir ie. `${HOME}/.config/nvim`
- Execute below set of commands to create neccessary file and Folder
```sh
mkdir -p ${XDG_CONFIG_HOME}/nvim/lua/plugins
mkdir -p ${XDG_CONFIG_HOME}/nvim/lua/custom
touch -p ${XDG_CONFIG_HOME}/nvim/init.lua

cd ${XDG_CONFIG_HOME}/nvim/lua/plugins
touch autopairs.lua barbicue.lua cmp.lua colorscheme.lua comments.lua conform.lua dap.lua harpoon.lua highlight.lua lint.lua lsp.lua lualine.lua markdown.lua mini.lua noice.lua nvimtree.lua snapshot.lua telescope.lua treesitter.lua gopher.lua gitsigns.lua

cd ${XDG_CONFIG_HOME}/nvim/lua
touch autocmds.lua keymaps.lua opts.lua 

cd ${XDG_CONFIG_HOME}/nvim/lua/custom
touch lsp.lua cmp.lua mason.lua
```
- After completing above set of commands you see structure of your directory looks exactly like below
```
 init.lua
 lua
├──  autocmds.lua
├──  keymaps.lua
├──  opts.lua
├──  custom
│   ├──  cmp.lua
│   ├──  lsp.lua
│   └──  mason.lua
└──  plugins
    ├──  autopairs.lua
    ├──  barbecue.lua
    ├──  cmp.lua
    ├──  colorscheme.lua
    ├──  comments.lua
    ├──  conform.lua
    ├──  dap.lua
    ├──  gitsigns.lua
    ├──  gopher.lua
    ├──  harpoon.lua
    ├──  highlight.lua
    ├──  lint.lua
    ├──  lsp.lua
    ├──  lualine.lua
    ├──  markdown.lua
    ├──  mini.lua
    ├──  noice.lua
    ├──  nvimtree.lua
    ├──  snapshot.lua
    ├──  telescope.lua
    └──  treesitter.lua
```
> init.lua is special file which is looked up by neovim to find the configuration where custom folder is related to tidying configuration code.
now plugins folder is where we are actually going to configure all of our plugins.

### Configuring keymaps
---
- To set keymap in neovim you can use vim api to do so `vim.keymap.set(mode, lhs, rhs, options)`
    - mode &rarr; normal/visual/insert(n/v/i) any of this or all using lua table syntax `{"i", "v", "n"}`
    - lhs &rarr; whatever keys you want to set
    - rhs &rarr; actual command, lua function or any other keymap you want to override
    - options &rarr; accepts lua table generally you can provider buffer number and description but it's optional
- Put eveything below in `lua/keymaps.lua` file. all keymaps are self explained by comments description field 
```lua
vim.keymap.set("n", "<Esc>", "<cmd>nohlsearch<CR>")
vim.keymap.set("i", "jj", "<Esc>")
vim.keymap.set({ "n", "i" }, "<C-s>", "<cmd>w<cr>", { silent = true })
vim.keymap.set({ "n", "i" }, "<C-c>", "<cmd>bd!<cr>", { silent = true })

-- Diagnostic keymaps
vim.keymap.set("n", "[d", vim.diagnostic.goto_prev, { desc = "Go to previous [D]iagnostic message" })
vim.keymap.set("n", "]d", vim.diagnostic.goto_next, { desc = "Go to next [D]iagnostic message" })
vim.keymap.set("n", "<leader>e", vim.diagnostic.open_float, { desc = "Show diagnostic [E]rror messages" })
vim.keymap.set("n", "<leader>q", vim.diagnostic.setloclist, { desc = "Open diagnostic [Q]uickfix list" })

-- Window navigations keymap
vim.keymap.set("n", "<C-h>", "<C-w><C-h>", { desc = "Move focus to the left window" })
vim.keymap.set("n", "<C-l>", "<C-w><C-l>", { desc = "Move focus to the right window" })
vim.keymap.set("n", "<C-j>", "<C-w><C-j>", { desc = "Move focus to the lower window" })
vim.keymap.set("n", "<C-k>", "<C-w><C-k>", { desc = "Move focus to the upper window" })

-- Visual Mode yanking and pasting without delete result in it
vim.keymap.set("v", "p", '"_dP', { desc = "after yanking something it keeps in that register" 

-- nvim tree binding
vim.keymap.set("n", "<leader>ee", "<Cmd>NvimTreeToggle<CR>", { desc = "toggle nvim tree expolorer" })
vim.keymap.set(
	"n",
	"<leader>ef",
	"<Cmd>NvimTreeFindFile<CR>",
	{ desc = "open file focusing it and opening folder if neccessary" }
)

-- todo comments toggle
vim.keymap.set("n", "td", "<Cmd>TodoTelescope<CR>", { desc = "open todo in telescope" })
vim.keymap.set("n", "tdq", "<Cmd>TodoQuickFix<CR>", { desc = "open todo in quick fix list" })

-- quickfix list navigation
vim.keymap.set("n", "<C-n>", "<Cmd>cnext<CR>", { desc = "navigate forward in quickfix" })
vim.keymap.set("n", "<C-p>", "<Cmd>cprev<CR>", { desc = "navigate backward in quickfix" })

-- stay in indent mode in Visual
vim.keymap.set("v", "<", "<gv", { desc = "indent prev keeping in visual mode" })
vim.keymap.set("v", ">", ">gv", { desc = "indent next keeping in visual mode" })

-- move test up or down in visual mode
vim.keymap.set("v", "<A-j>", ":m '>+1<CR>gv=gv", { desc = "indent next keeping in visual mode" })
vim.keymap.set("v", "<A-k>", ":m '<-2<CR>gv=gv", { desc = "indent next keeping in visual mode" })

-- snapshots
vim.keymap.set("v", "<leader>cs", function()
	require("nvim-silicon").clip()
end, { desc = "copy screenshot to clipboard", silent = true })
vim.keymap.set("v", "<leader>cc", function()
	require("nvim-silicon").file()
end, { desc = "save screenshot as file", silent = true })
```

### Configuring options
---

### Adding autocommands
---

### Adding filetypes 
---

### Initaiting lazy loader
---
lazy is plugin used to install other plugins in neovim it's like you have to use `nvim autocmd` in order to load lazy plugin at startup. follow along with below code and you will know

```sh linenums="1"
local lazypath = vim.fn.stdpath 'data' .. '/lazy/lazy.nvim'
if not vim.loop.fs_stat(lazypath) then
  local lazyrepo = 'https://github.com/folke/lazy.nvim.git'
  vim.fn.system { 'git', 'clone', '--filter=blob:none', '--branch=stable', lazyrepo, lazypath }
end 
vim.opt.rtp:prepend(lazypath)
```

1. line 1 &rarr; sets lazypath for lazy plugins to be loaded or searched
2. line 2 &rarr; checks if lazy plugin is present at path given if not then proceed
3. line 3&4 &rarr; clone the lazyrepo using vim system function on given std path
4. line 6 &rarr; `opt.rtp:prepend(lazypath)` means initiate directory path for searching neovim runtime files

### configuring statusline using lualine
---

### configuring file explorer using nvim-tree
---

### adding theme and colorscheme
---

### adding syntax highlight with nvim-treesitter
---

### setting up formatter using conform 
---

### setting up autocompletion using nvim-cmp
---

### setting up lsp using lspconfig
---

### setting up linter using nvim-lint
---

### setting up debugging using nvim-dap
---

