# cs423-programming-assignment
Run the code with either python .\gui_highlighter.py or python3 .\gui_highlighter.py depending on python installation
Button nodes are highlighted in yellow while other nodes are highlighted in red

Input data is stored in the 'data' directory
Output is stored in the 'output' directory

# Design Choices:
Originally I planned on using an xml parser to extract node attributes. However, the parser fails on files with improper closing tags. Because the scope of this script is quite simple, I parsed through the xml files myself and created a hashmap of nodes associated with a nested hashmap of certain attributes. Currently I am only storing the bounds and clickable attributes but this script can easily be extended to include any other attributes. The bounds are used to locate every leaf node while the clickable attribute is used to help visually distinguish between a clickable and non-clickable element. I only used a different color with thicker lines to color the clickable element for simplicity's sake.

If I were to refactor/redo this script, I would use RegEx to parse through the XML and extract every leaf node along with every attribute. Within a larger scope, I would also make the code mode readable using RegEx.