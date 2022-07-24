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

const interestFreqDict = {
    "programming." : 3,
    "algorithms." : 3,
    "software engineering." : 3,
    "robotics." : 2,
    "startups." : 3,
    "mathematics." : 3,
    "statistics." : 1,
    "data." : 2,
    "data science." : 2,
    "web development." : 1,
    "computer science." : 1,
    "software." : 1,
    "computers." : 1,
    "finance." : 1,
    "Python." : 1,
    "Java." : 1,
    "C." : 1,
    "Haskell." : 1,
    "Kotlin." : 1,
    "engineering." : 3,
    "tech." : 3,
    "technology." : 3,
    "full-stack development." : 2,
}

var interests = []
for (i in interestFreqDict) {
    for (j = 0; j < interestFreqDict[i]; j++) interests.push(i);
}
console.log(interests)

var currentInterestIndex;
var lastBuffer = [];
var interestWordIndex;
var intervalVal;

function nextWord() {
    var repeat = true;
    while (repeat) {
        currentInterestIndex = Math.floor(Math.random() * interests.length);
        repeat = lastBuffer.includes(interests[currentInterestIndex]);
    }
    if (lastBuffer.length >= noRepeatBufferLength) lastBuffer.shift();
    lastBuffer.push(interests[currentInterestIndex]);
    interestWordIndex = 0;
}

nextWord();

function generateInterval(mode) {
    var speed = Math.floor(Math.random() * (typeSpeedRange[1] - typeSpeedRange[0])) + typeSpeedRange[0];
    if (mode === "DELETE") speed *= deleteSpeedMultiplier;
    return 60000 / speed;
}

function type() {
    var text = interests[currentInterestIndex].substring(0, interestWordIndex + 1);
    interestEl.innerHTML = text;
    interestWordIndex++;
    if (text === interests[currentInterestIndex]) {
        clearInterval(intervalVal);
        setTimeout(function () {
            intervalVal = setInterval(delete_text, generateInterval("DELETE"));
        }, textShownTime);
    }
}

function delete_text() {
    var text = interests[currentInterestIndex].substring(0, interestWordIndex - 1);
    interestEl.innerHTML = text;
    interestWordIndex--;

    if (text === '') {
        clearInterval(intervalVal);

        nextWord();
        
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