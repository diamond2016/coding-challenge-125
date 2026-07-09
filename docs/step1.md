In this step your goal is to compute and display a basic line-level diff between two text inputs.

Create a simple interface with two text areas for input and a diff button. When the user clicks the button, your tool should compute the diff between the two inputs and display the result. Colour-code additions in green, deletions in red, and leave unchanged lines uncoloured or in a neutral colour.

At this stage a simple vertical, unified-style output is fine - we'll add proper views in the next steps.

I prefer to create three area, one for text 1, one for tecxt 2 and athiord for diff text2 - text1.

Layout as follows 

- - - - - - - - - - - - - - - - - - - - - 
<logo>   <Load text1> <Load Text2>  <Diff>      <--- header
- - - - - - - - - - - - - - - - - - - - - 

text area 1     |   text area 2 
                |
                |
                |
                |
                |
                |

text area diff  |   list operations
                |
                !
                |
                |
                |
                |


- - - - - - - - - - - - - - - - - - - - - 
heeder: component with the three buttons: "Load text 1". "Load text 2", "Diff"
text area 1, text area 2, text area diff: three components, same size, which contains only a single text field, capabie of multiline 
list operations same size of text area but list item that will contain the list of operations of tipe "op" "text"
