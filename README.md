# sublime-plugins-dump
A place to dump all of those small, useless, handmade plugins

## Rename File
Bind the `F2` key to renam the file.

## Dashline
Bind `ctrl+shift+keypad_minus` to add a line of `-` under the selected lines, matching the length of said lines.
`ctrl+alt+shift+keypad_minus` lets the user chose another character than `-`.

## Surround Title
Bind `ctrl+shift+keypad_multiply` to surround with `#` the selected lines.
`ctrl+alt+shift+keypad_multiply` lets the user chose another character than `#`.

## Jump To Title
Bind `ctrl+t` to allow the user to jump to a title defined with previous plugins.
Transpose rebound to `ctrl+alt+t`.

## Find Over Expand
Bind `ctrl+shift+d` do the opposite of `ctrl+d`.
Duplicate line rebound to `ctrl+alt+d`.

## Number
Bind `super+keypad_minus` to number the selected lines.
`super+alt+keypad_minus` lets the user choose the character to follow the numbers, and which number to start from.

## Sum
Bind `ctrl+=` to display the sum of the selected numbers.

## Group Navigation
Bind `ctrl+tab` and `ctrl+shift+tab` to navigate logically between the tabs of a group.

## Unwrap
Bind `ctrl+alt+m` to unwrap the selection.

## Duplicate File
Add a "Duplicate File" option to the context menu.
The name of the copy will be the name of the original file, followed by an underscore and the timestamp.
If the targeted file is a symlink, the copy will not be one.

## Close Views
Bind `ctrl+shift+f4` to close all views in the active group but the active one.
Bind `ctrl+k, ctrl+f4` to close all views in the active group.
Bind `ctrl+k, shift+f4` to close all views in the active window but the active one.
Bind `ctrl+k, ctrl+shift+f4` to close all views in the active window.

## Split Line
Bind `alt+enter` to split a line. If the selection is a point, the text on the right part of the cursor is sent to a new line above. Otherwise, the selected region is sent.

## Go fmt on save
Add an event plugin to run `go fmt` when saving golang files.

## Go to pointer
Bind `ctrl+k, ctrl+x` to mimic the ctrl+xx functionality of bash.

## Copy to
Bind `ctrl+shift+c` to copy to EOL, `ctrl+k, ctrl+shift+c` to copy to BOL.
Bind `ctrl+shift+x` to cut to EOL, `ctrl+k, ctrl+shift+x` to cut to BOL.

## Gist
Add a "Gist" command to quickly insert some gist.

## Reverse single selection
Bind `shift+escape` to deselect every region except the last one.
