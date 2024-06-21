const form = document.querySelector('#inviteForm');
const input = document.querySelector('input');
const main = document.querySelector('.main');
const ul = document.querySelector('#invitedList');

/*
1. create li
------------
*/ 
function createLi() {
  const li = document.createElement('li');
  const span = document.createElement('span');
  span.textContent = input.value;

  const label = document.createElement('label');
  label.textContent = 'confirmed';

  const label_time = document.createElement('label');
  label.textContent = tasktime.value
  
  const editBtn = document.createElement('button');
  editBtn.textContent = 'edit';
  const removeBtn = document.createElement('button');
  removeBtn.textContent = 'remove';

  li.appendChild(span);
  li.appendChild(label);
  label.appendChild(label_time);
  li.appendChild(editBtn);
  li.appendChild(removeBtn);

  return li;
}

form.addEventListener('submit', (event) => {
  event.preventDefault();

  const li = createLi();

  if(input.value === '') {
    alert('Enter the name please!!!');
  } else {
    ul.appendChild(li);
  }
}); 


/*
3. Button actions
-----------------
*/ 
ul.addEventListener('click', (event) => {
  if(event.target.tagName === 'BUTTON') {
    const button = event.target;
    const li = button.parentNode;
    const ul = li.parentNode;

    if(button.textContent === 'remove') {
      ul.removeChild(li);
    } 
    else if(button.textContent === 'edit') {
      const span = li.firstElementChild;
      const input = document.createElement('input');
      input.type = 'text';
      input.value = span.textContent;
      input.type = 'text';
      input.value = span.textContent;


      li.insertBefore(input, span);
      li.removeChild(span);
      button.textContent = 'save';
    } 
    
    else if(button.textContent === 'save') {
      const input = li.firstElementChild;
      const span = document.createElement('span');
      span.textContent = input.value;

      const span_dt = document.createElement('span');
      span_dt.textContent = tasktime.value;

      li.insertBefore(span, span_dt, input);
      li.removeChild(input);
      button.textContent = 'edit';
    }
  }
});

/*
4. create and append elements
-----------------------------
*/ 
const div = document.createElement('div');
div.className = 'showHide';
const filterLabel = document.createElement('label');
filterLabel.textContent = 'Hide those who have not responded';
const filtertime = document.createElement('label');

div.appendChild(filterLabel);
filterLabel.appendChild(filtertime);
main.insertBefore(div, ul);

filterCheckbox.addEventListener('change', (event) => {
  const isChecked = event.target.checked;
  const lis = ul.children;

  if(isChecked) {
    for(let i = 0; i < lis.length; i++) {
      var li = lis[i];

      if(li.className === 'responded') {
        li.style.display = '';
      } else {
        li.style.display = 'none';
      }
    }
  } else {
    for(let i = 0; i < lis.length; i++) {
      var li = lis[i];
      li.style.display = '';
    }
  }
});