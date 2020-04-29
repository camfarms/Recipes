//Setting up Div
var idGraph = 0;
function setupGraphDiv(){
   ++idGraph;
   //creating div and remove button
   div = createGraphDiv();
   button = createRemoveButton(); 

   //add to the div with the id graphContainer
   $("#recipeContainer").append(div).append(button);
}

/**
 * Should NEVER call except in setupGraphDiv()
 */
function createGraphDiv(){
   div = document.createElement('div');
        div.id = "Recipe" + idGraph.toString();
        div.style = "height: 300px; width: 100%;";
        div.class = 'remove';
   return div;
}

/**
 * Should NEVER call except in setupGraphDiv()
 */
function createRemoveButton(){
   button = document.createElement('button'); 
   button.id = idGraph.toString();
   button.setAttribute("value", "Remove");

   button.onclick = (function(){ 
       var graphDiv = document.getElementById("Recipe" + this.id.toString());
       var buttonDiv = document.getElementById(this.id.toString());
       buttonDiv.parentNode.removeChild(buttonDiv);
       graphDiv.parentNode.removeChild(graphDiv); 
        
    })
    return button;
}