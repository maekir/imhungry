$(document).ready(function(){
    var search_ingredients = $("#ingredient_search");
        ingredients_all = $(".ingredient_buttons *");
        
    ingredients_all.hide();

    search_ingredients.on("keyup", function() {
        var value = $(this).val().toLowerCase();

        ingredients_all.filter(function() {
            $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1);
        }).show();

        if (value == '') 
            ingredients_all.hide();
    });
});
