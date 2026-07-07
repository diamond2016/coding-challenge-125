Coding Challenge #125 - Online Diff Viewer
This challenge is to build your own online diff viewer.
John Crickett
Jul 04, 2026

Coding Challenge #125 - Online Diff Viewer
This challenge is to build your own online diff viewer that compares two text inputs and displays the differences in a clear, visual format.

If you’ve ever used GitHub, GitLab, or any code review tool, you’ve seen a diff viewer. It’s the side-by-side or unified view that shows you exactly what changed between two versions of a file - green for additions, red for deletions. But how do these tools actually work? In this challenge you’ll find out by building one yourself. You’ll implement a diff algorithm, render the results in multiple visual formats, and add all the quality-of-life features that make a diff viewer truly useful.

The Challenge - Building Your Own Online Diff Viewer
You’re going to build an online diff viewer that runs entirely in the browser. Users will paste, upload, or drag-and-drop two pieces of text, and your tool will show them exactly what changed. Over several steps you’ll add side-by-side and unified views, syntax highlighting, navigation tools, export options, and accessibility features.

Step Zero
In this introductory step you’re going to set your environment up ready to begin developing and testing your solution.

This is a web application, so you’ll need HTML, CSS, and JavaScript (or a framework you’re comfortable with). You’ll also need to understand how a diff algorithm works.

Take some time to study the Myers diff algorithm. It’s the algorithm used by Git and many other tools. Your diff viewer will need to take two sequences of lines, compute the shortest edit script that transforms one into the other, and produce a set of additions, deletions, and unchanged lines.

Step 1
In this step your goal is to compute and display a basic line-level diff between two text inputs.

Create a simple interface with two text areas for input and a diff button. When the user clicks the button, your tool should compute the diff between the two inputs and display the result. Colour-code additions in green, deletions in red, and leave unchanged lines uncoloured or in a neutral colour.

At this stage a simple vertical, unified-style output is fine - we’ll add proper views in the next steps.

Testing: Paste the following into your two inputs:

Left (original):

function greet(name) {
  console.log("Hello, " + name);
}

function farewell(name) {
  console.log("Goodbye, " + name);
}
Right (modified):

function greet(name) {
  console.log("Hello, " + name + "!");
  console.log("Have a great day!");
}

function farewell(name) {
  console.log("Goodbye, " + name + "!");
}
You should see the added lines in green and any lines that exist only in the original in red. Unchanged lines like function greet(name) { should appear without colour.

Step 2
In this step your goal is to add a side-by-side diff view with properly aligned rows.

Side-by-side views show both inputs next to each other, with matching lines on the same row and gaps where lines were added or removed. This is the most intuitive way to view diffs for many people.

Your side-by-side view should:

Show the original on the left and the modified version on the right.

Align unchanged lines on the same row.

Leave blank gaps on one side when lines are added or removed.

Show line numbers for both sides.

Testing: Use the same test data from Step 1. In the side-by-side view, the two console.log lines in the modified version should appear opposite blank space on the left, and the original console.log("Goodbye, " + name) line should appear opposite blank space on the right.

Step 3
In this step your goal is to implement a unified diff view and let users toggle between the two views.

The unified diff view is the format used by Git and many command-line tools. It shows a single continuous output where additions are prefixed with +, deletions with -, and context lines with a space. Hunks are separated by @@ headers showing the line ranges.

Your tool should allow the user to switch between side-by-side and unified views with a simple toggle button or tab.

Testing: Switch between views with the same test data. In unified view, verify that added lines start with +, deleted lines with -, and context lines with a space. The hunk header format should show something like @@ -2,5 +2,6 @@.

Step 4
In this step your goal is to display diff summary statistics.

Users want to quickly understand the scope of changes. Your viewer should show a summary panel that displays:

Lines added

Lines removed

Lines unchanged

Total number of changes

Update this summary whenever the diff is recomputed.

Testing: With the test data from Step 1, verify your summary shows 2 lines added, 1 line removed, and the correct number of unchanged lines. Change the inputs and confirm the statistics update accordingly.

Step 5
In this step your goal is to add syntax highlighting for at least five common programming languages.

Diff output is much easier to read when the code is syntax-highlighted. Your tool should highlight at least JavaScript, Python, HTML, CSS, and JSON.

The syntax highlighting should apply to both the original and modified sides. It should also work with the colour coding from the diff - so a highlighted Python keyword that appears in an added line would show with both the syntax colour and a green background.

Your viewer should attempt to auto-detect the language based on file extension or content, and also allow the user to manually override the language selection.

Testing: Create test files in each supported language and verify the highlighting works correctly. Try mixing file types (JavaScript on the left, Python on the right) and verify the language override lets you pick the correct one. Test auto-detection by uploading a .py file and confirming Python highlighting is applied.

Step 6
In this step your goal is to support multiple input methods for loading text into the diff viewer.

Typing or pasting into text areas works, but users will also want to:

Upload files from their computer using a file picker.

Drag and drop files directly onto the viewer.

Fetch content from a URL.

When a file is loaded, display basic metadata such as the filename, file size, detected language, and line count.

Testing: Create two text files on your computer and upload them using the file picker. Verify the content appears correctly in both sides and the metadata is displayed. Test drag and drop by dragging a file from your desktop onto the viewer. Test URL fetch by providing the URL of a publicly accessible text file.

Step 7
In this step your goal is to add diff precision modes: smart, word, and character-level highlighting.

So far your diff works at the line level. But within a changed line, only part of the line might have changed. Precision modes let users see exactly which words or characters changed:

Smart mode: Your best guess at what changed - typically word-level changes.

Word mode: Highlight changed words within a line.

Character mode: Highlight individual changed characters within a line.

Testing: Use a line like changing Hello World to Hello Universe. In word mode, only World should be highlighted on the left and Universe on the right. In character mode, individual characters like W vs U should be highlighted. Verify smart mode makes a sensible choice.

Step 8
In this step your goal is to add diff control options that let users customise what counts as a change.

Sometimes you want to focus on meaningful changes and ignore formatting differences. Add toggleable options for:

Ignoring whitespace changes (e.g., extra spaces that don’t affect the code).

Ignoring case differences (e.g., HELLO vs hello).

Ignoring blank lines (empty lines added or removed).

Ignoring indentation-only changes (tabs vs spaces, changes in indent level).

Ignoring line ending differences (CRLF vs LF).

These options should be available as checkboxes or a settings panel and take effect immediately when changed.

Testing: Create two inputs that differ only in whitespace. With “ignore whitespace” enabled, the diff should show no changes. Disable it and the changes should reappear. Repeat for each option.

Step 9
In this step your goal is to improve large diff readability by letting users hide unchanged sections.

When there are hundreds of lines of unchanged code between changes, scrolling through all of them is tedious. Add the ability to collapse unchanged sections, showing a clickable indicator like “... 47 unchanged lines ...”. Users should be able to click the indicator to expand the section.

Testing: Create two files with at least 50 unchanged lines between two change blocks. Verify the middle section is collapsed by default or can be collapsed, and that clicking it expands to show the full content.

Step 10
In this step your goal is to add a line wrap toggle and synchronised scrolling.

When lines are long, users need to be able to toggle line wrapping on and off. With wrapping off, a horizontal scrollbar lets them view long lines without breaking formatting.

Synchronised scrolling keeps both sides of the side-by-side view scrolling together. When the user scrolls one pane, the other follows. Users should also be able to disable this if they prefer independent scrolling.

Testing: Create a file with very long lines (200+ characters) and verify toggling line wrap works correctly. In side-by-side view, scroll one pane and verify the other scrolls in sync. Disable sync scrolling and verify the panes scroll independently.

Step 11
In this step your goal is to add comprehensive navigation features.

Navigating a large diff efficiently is critical. Add the following:

Next change and previous change buttons that jump between diff hunks.

First change and last change buttons that jump to the start and end of the diff.

A change navigator panel that lists all change blocks, showing the line range and a preview. Clicking a block in the panel should jump to that location.

Gutter markers (coloured indicators in the margin) for additions, deletions, and modifications.

Keyboard shortcuts for all navigation actions (e.g., J for next, K for previous).

Testing: Create a diff with at least 10 change blocks spread across the document. Verify each navigation control works correctly. Test all keyboard shortcuts and confirm the change navigator panel updates to highlight the current change as you navigate.

Step 12
In this step your goal is to handle large inputs efficiently.

Diffs of 10,000+ lines can freeze the browser if not handled carefully. To keep the UI responsive:

Run the diff computation in a Web Worker so the main thread stays responsive.

Use virtualised rendering - only render the lines currently visible in the viewport instead of all 10,000 at once.

Show a progress indicator while the diff is being computed.

Testing: Generate two large text files (10,000+ lines) with differences scattered throughout. Verify the diff computation doesn’t freeze the browser - you should be able to click buttons and scroll while it’s processing. Verify scrolling through the output is smooth.

Step 13
In this step your goal is to add export and copy options.

Users need to get the diff output out of your tool and into other tools or documents. Add the ability to:

Copy the full diff output to the clipboard.

Copy individual change blocks.

Export the diff as a unified patch file, HTML, Markdown, and JSON.

Generate Git-compatible patch output that can be applied with git apply.

Testing: Create a diff and test each export format. For unified patch, verify you can save it to a file and apply it with git apply. For HTML and Markdown, verify the output renders correctly with colour coding preserved. For JSON, verify the structure includes all change information.

Step 14
In this step your goal is to make your diff viewer a Progressive Web App (PWA) that works offline.

Turn your diff viewer into a PWA with a service worker so users can use it without an internet connection. Additionally:

Persist the user’s recent sessions using localStorage or IndexedDB.

Show a history of previous diffs the user can revisit.

Let users save named diff sessions they can come back to later.

Testing: Load your diff viewer, then disconnect from the internet. Verify the page still loads and the diff viewer works. Run some diffs, close the browser, reopen it offline, and verify your history is still there.

Step 15
In this step your goal is to ensure your diff viewer is fully accessible and works well on all devices.

Your viewer should be usable by everyone, regardless of ability or device. This means:

All functionality should be keyboard-accessible.

Proper ARIA labels and roles should be used throughout.

Screen readers should announce change summaries when the diff is computed.

Line numbers and file headers should remain visible (stick to the top) when scrolling.

The layout should be responsive - usable on desktop, tablet, and mobile.

Clear empty states and error messages should be shown when something goes wrong.

Testing: Navigate the entire viewer using only the keyboard. Run a screen reader and verify it announces the diff results. Resize the browser to mobile width and verify everything remains usable. Test with an empty input to verify the empty state message is shown.

Step 16
In this step your goal is to add theme support with light, dark, and high-contrast modes.

Your diff viewer should respect the user’s system theme preference by default. Add a theme selector that lets users choose between:

Light mode

Dark mode

High-contrast mode (for users with visual impairments)

The theme should apply to all UI elements including the diff output, syntax highlighting colours, and control panels.

Testing: Change your system theme and verify the viewer matches. Manually switch themes and verify all colours update correctly. Test high-contrast mode with a screen reader or accessibility testing tool.

Going Further
Once you’ve built the core diff viewer, consider adding these advanced features:

AI-powered diff explanation: Use an LLM to explain what a change does in plain English.

Code-review mode: Let users add comments and annotations to specific lines or change blocks.

Semantic diffs: For JSON, compare the structure rather than the text. The same for HTML - compare the DOM tree.

Syntax validation: Highlight JSON or HTML that is syntactically invalid in the input.

Three-way merge view: Show a base version and two modified versions, useful for resolving merge conflicts.

Image diff: Support uploading two images and showing a visual diff (pixel-by-pixel or structural comparison).
