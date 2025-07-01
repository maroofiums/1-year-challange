count = 0;

const increaseBtn = document.querySelector('#increase')
const Display = document.querySelector('#count')
const descreaseBtn = document.querySelector('#decrease')
const resetBtn = document.querySelector('#reset')

function updatedisplay (){
    Display.textContent = count;
    if (count > 0){
        Display.style.color = 'green';
    } else if(count < 0) {
        Display.style.color = 'red';
    }else {
        Display.style.color = 'black';
    }
}

increaseBtn.addEventListener('click', () => {
    count++;
    updatedisplay();
});

descreaseBtn.addEventListener('click',()=>{
    count--;
    updatedisplay();
})

resetBtn.addEventListener('click',()=>{
    count = 0;
    updatedisplay();
})