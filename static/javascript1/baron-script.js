window.onload = function() {
    // Horizontal
    baron({
        root: '.main__clipper',
        scroller: '.main__scroller',
        bar: '.main__bar',
        scrollingCls: '_scrolling',
        draggingCls: '_dragging',
        direction: 'h'
    });

    baron({
        root: '.baron',
        scroller: '.baron__scroller',
        bar: '.baron__bar',
        scrollingCls: '_scrolling',
        draggingCls: '_dragging'
    }).fix({
        elements: '.header__title',
        outside: 'header__title_state_fixed',
        before: 'header__title_position_top',
        after: 'header__title_position_bottom',
        clickable: true
    }).controls({
        // Element to be used as interactive track. Note: it could be different from 'track' param of baron.
        track: '.baron__track',
        forward: '.baron__down',
        backward: '.baron__up'
    });

    //HelenGor
    document.getElementById("card-blocks-menu").addEventListener("click",function(event){
        var indexElement = [].indexOf.call(this.children, event.target);
        var menuItems = document.getElementById("card-blocks-menu").getElementsByClassName("card-blocks-menu-item");
        var BlocskObj = document.getElementById("card-blocks-wrap").getElementsByClassName("card-block");
        for (var i=0; i<BlocskObj.length; i++){
            BlocskObj.item(i).className = "card-block";
            menuItems.item(i).className = "card-blocks-menu-item";
        }
        BlocskObj.item(indexElement).className = "card-block card-block-active";
        menuItems.item(indexElement).className = "card-blocks-menu-item card-blocks-menu-item-active";
    });

    var cardBlocks = document.getElementsByClassName("baron__scroller");
    for (var i=0; i<cardBlocks.length; i++){
        cardBlocks.item(i).addEventListener("scroll",function(){
            if(this.scrollTop > 30){
                this.parentNode.getElementsByClassName("card-block-gradient-up").item(0).style.display = "block";
            }else{
                this.parentNode.getElementsByClassName("card-block-gradient-up").item(0).style.display = "none";
            }
        });
    }

};