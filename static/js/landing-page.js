const animateTypeUp = el => {
    const overallString = "hello_world();";
    const overallStringLength = overallString.length;

    const animationDuration = 800;
    const totalFrames = overallStringLength;
    const frameDuration = animationDuration / totalFrames;

    let frame = 0;
    const counter = setInterval(
        () => {
            frame++;
            const progress = frame / totalFrames;
            const currentCount = overallString.substring(0, overallStringLength * progress);

            if (el.textContent !== currentCount) {
                el.textContent = currentCount;
            }

            if (frame === totalFrames) {
                clearInterval(counter);
            }
        }, frameDuration
    );
}

const typeSpeedRange = [900, 1000]; // cpm
const textShownTime = 1500;
const textNotShownTime = 100;
const deleteSpeedMultiplier = 2;
const noRepeatBufferLength = 5;
const interestEl = document.getElementById("interests");

const interests = [
    "programming.",
    "algorithms.",
    "software engineering.",
    "robotics.",
    "startups.",
    "mathematics.",
    "statistics.",
    "data.",
    "data science.",
    "web development.",
    "computer science.",
    "software.",
    "computers.",
    "finance.",
    "Python.",
    "Java.",
    "C.",
    "Haskell.",
    "Kotlin.",
    "engineering.",
    "tech.",
    "technology.",
    "full-stack development."
]


function fy_shuffle(arr) {
    // Durstenfeld/Knuth's implementation of the
    // Fisher-Yates shuffle
    for (var i = arr.length - 1; i > 0; i--) {
        j = Math.floor(Math.random() * (i + 1));
        var temp = arr[j];
        arr[j] = arr[i];
        arr[i] = temp;
    }
}

fy_shuffle(interests);

function modified_fy_shuffle(arr) {
    // puts the shuffled array in the front
    // prevents the last 25% of the previous array
    // from being in the first 25% of the next array
    //
    // while this restricts the randomness of the next shuffle
    // by making it dependent on the previous shuffle, the alternatives
    // are to just use one shuffle repeatedly, in which case each shuffle
    // is completely dependent on the first shuffle, or to allow repeats
    // at the starts and ends of shuffles, which defeats the entire purpose
    // of using shuffling rather than completely randomly drawing.
    var fourth = Math.floor(arr.length / 4);
    for (var i = 0; i < fourth; i++) {
        j = Math.floor(Math.random() * (arr.length - fourth - i + 1)) + i;
        var temp = arr[j];
        arr[j] = arr[i];
        arr[i] = temp;
    }
    for (var i = fourth; i < arr.length - 1; i++) {
        j = Math.floor(Math.random() * (arr.length - i)) + i;
        var temp = arr[j];
        arr[j] = arr[i];
        arr[i] = temp;
    }
}

var interestWordIndex = 0;
var intervalVal;
var counter = 0;

function nextWord() {
    word = interests[counter];
    if (counter == interests.length - 1) {
        modified_fy_shuffle(interests);
        counter = 0;
    } else {
        counter++;
    }
    return word;
}

var currentWord = nextWord();

function generateInterval(mode) {
    var speed = Math.floor(Math.random() * (typeSpeedRange[1] - typeSpeedRange[0])) + typeSpeedRange[0];
    if (mode === "DELETE") speed *= deleteSpeedMultiplier;
    return 60000 / speed;
}

function type() {
    var text = currentWord.substring(0, interestWordIndex + 1);
    interestEl.innerHTML = text;
    interestWordIndex++;
    if (text === currentWord) {
        clearInterval(intervalVal);
        setTimeout(function () {
            intervalVal = setInterval(delete_text, generateInterval("DELETE"));
        }, textShownTime);
    }
}

function delete_text() {
    var text = currentWord.substring(0, interestWordIndex - 1);
    interestEl.innerHTML = text;
    interestWordIndex--;

    if (text === '') {
        clearInterval(intervalVal);

        currentWord = nextWord();
        
        setTimeout(function () {
            intervalVal = setInterval(type, generateInterval("TYPE"));
        }, textNotShownTime);
    }
}

setTimeout(function() {
    animateTypeUp(document.getElementById("title_typeup"));
}, 200);
setTimeout(function() {
    intervalVal = setInterval(type, generateInterval("TYPE"));
}, 7000);

// scrolldownbutton = document.getElementById("arrow-container");
// if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20)
//     scrolldownbutton.style.opacity = 0;
// else
//     scrolldownbutton.style.opacity = 1;

// function scrollFunction() {
//     if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20)
//         scrolldownbutton.style.opacity = 0;
//     else
//         scrolldownbutton.style.opacity = 1;
// }

// window.onscroll = function() {
//     scrollFunction();
// };