" Vim syntax file
" Language:	Help file
"   Adapted from help.vim.

" Remove any old syntax stuff hanging around
syn clear

syn match   hldhelpHeadline		"^[A-Z ]\+[ ]\+\*"me=e-1
syn match   hldhelpSectionDelim		"=\{3,}"
syn match   hldhelpSectionDelim		"-\{3,}"
syn match   hldhelpExampleStart		"^>" nextgroup=hldhelpExample
syn match   hldhelpExample		".*" contained
syn match   hldhelpHyperTextJump	"|[#-)!+-~]\+|"
syn match   hldhelpHyperTextEntry	"\*[#-)!+-~]\+\*\s"he=e-1
syn match   hldhelpHyperTextEntry	"\*[#-)!+-~]\+\*$"
syn match   hldhelpHeader		".*\~$"me=e-1 nextgroup=hldhelpIgnore
syn match   hldhelpIgnore		"." contained
syn keyword hldhelpNote			Note: NOTE: WARNING: Warning:
syn region  hldhelpNotVi		start="{Vi[: ]" start="{not" start="{only" end="}" contains=helpLeadBlank,helpHyperTextJump
syn match   hldhelpLeadBlank		"^\s\+"

if !exists("did_hldhelp_syntax_inits")
  let did_hldhelp_syntax_inits = 1

  hi link hldhelpExampleStart    helpIgnore
  hi link hldhelpIgnore          Ignore
  hi link hldhelpHyperTextJump   Subtitle
  hi link hldhelpHyperTextEntry  String
  hi link hldhelpHeadline        Statement
  hi link hldhelpHeader          PreProc
  hi link hldhelpSectionDelim    PreProc
  hi link hldhelpVim             Identifier
  hi link hldhelpExample         Comment
  hi link hldhelpOption          Type
  hi link hldhelpNotVi           Special
  hi link hldhelpSpecial         Special
  hi link hldhelpNote            Todo
  hi link Subtitle               Identifier
endif

let b:current_syntax = "hldhelp"

" vim: ts=8 noet
