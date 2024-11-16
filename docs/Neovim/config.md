---
tags:
    - golang
    - ide
    - neovim
    - lsp
---

This is the complete tutorial to configure neovim to work with golang and some other language as IDE. we will explore some options and how neovim plugin system works as well lsp client and mason for installing our dependencies. If you are really new to vim/neovim ecosystem I recommend you to get familier with neovim using `:Tutor` and you can also refer to awesome [nvim kickstarter](https://github.com/nvim-lua/kickstart.nvim). Refer all the comments and try to modify some things your liking.

# How to proceed with configuration

## configuring keymaps

## configuring options

## adding autocommands

## Initaiting lazy loader

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

## adding filetypes 

## configuring statusline using lualine

## configuring file explorer using nvim-tree

## adding theme and colorscheme

## adding syntax highlight with nvim-treesitter

## setting up formatter using conform 

## setting up autocompletion using nvim-cmp

## setting up lsp using lspconfig

## setting up linter using nvim-lint

## setting up debugging using nvim-dap


