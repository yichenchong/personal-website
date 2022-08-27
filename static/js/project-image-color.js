var projects = document.getElementsByClassName("project-square")


var imagesLoaded = 0;
var totalImages = $("img").length;

$("img").each(function (_idx, img) {
    $("<img>").on("load error", imageLoaded).attr("src", $(img).attr("src"));
});
function imageLoaded() {
    imagesLoaded++;
    if (imagesLoaded == totalImages) {
        colorImages();
    }
}

function colorImages() {
    for (var i = 0; i < projects.length; i++) {
        var projectEl = projects[i];
        var imgEl = projectEl.getElementsByClassName("project-image")[0];
        var projectSquareFront = projectEl.getElementsByClassName("project-square-front")[0];
        while (!imgEl.complete) {}
        var projectSquareBack = projectEl.getElementsByClassName("project-square-back")[0];
        var rgb = getAverageRGB(imgEl);
        var avgColor = 'rgb('+rgb.r+','+rgb.g+','+rgb.b+')';
        projectSquareFront.style.backgroundImage = "radial-gradient(" + avgColor + "50%, #888 100%)";
        var bgLuminance = luminance(rgb.r / 2, rgb.g / 2, rgb.b / 2);
        var highestDark = (2 * bgLuminance - 0.35) / 9
        var lowestLight = ((9 * bgLuminance + 0.35) / 2);
        if (lowestLight < 1) projectSquareBack.style.color = 'white';
        else if (highestDark > 0) projectSquareBack.style.color = 'black';
        else console.log("Can't find colour");
        projectSquareBack.style.backgroundColor = 'rgb('+rgb.r / 2+','+rgb.g / 2+','+rgb.b / 2+')';
    }
}

function luminance(rs, gs, bs) {
    function transform(cs) {
        cs /= 255;
        var c;
        if (cs <= 0.03928) {
            c = cs / 12.92;
        } else {
            c = ((cs + 0.055) / 1.055) ** 2.4;
        }
        return c;
    }
    var r = transform(rs);
    var g = transform(gs);
    var b = transform(bs);
    var l = 0.2126 * r + 0.7152 * g + 0.0722 * b;
    return l;
}

function getAverageRGB(imgEl) {
    
    var blockSize = 1, // only visit every 5 pixels
        defaultRGB = {r:0,g:0,b:0}, // for non-supporting envs
        canvas = document.createElement('canvas'),
        context = canvas.getContext && canvas.getContext('2d'),
        data, width, height,
        i = -4,
        length,
        rgb = {r:0,g:0,b:0},
        count = 0;
        
    if (!context) {
        return defaultRGB;
    }
    
    height = canvas.height = imgEl.naturalHeight || imgEl.offsetHeight || imgEl.height;
    width = canvas.width = imgEl.naturalWidth || imgEl.offsetWidth || imgEl.width;
    try {
        context.drawImage(imgEl, 0, 0);
    } catch(e) {
        return defaultRGB;
    }
    
    try {
        data = context.getImageData(0, 0, width, height);
    } catch(e) {
        return defaultRGB;
    }
    
    length = data.data.length;
    
    while ( (i += blockSize * 4) < length ) {
        ++count;
        rgb.r += data.data[i];
        rgb.g += data.data[i+1];
        rgb.b += data.data[i+2];
    }
    
    // ~~ used to floor values
    rgb.r = ~~(rgb.r/count);
    rgb.g = ~~(rgb.g/count);
    rgb.b = ~~(rgb.b/count);
    console.log(rgb);
    
    return rgb;
}