(function () {
    var calc = function () {
        var docElement = document.documentElement;
        var clientWidthValue = docElement.clientWidth >1080?1080:docElement.clientWidth;
        docElement.style.fontSize = 10*(clientWidthValue/540) +'px';
    }
    calc();
    window.addEventListener('resize',calc());
})();