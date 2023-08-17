

var students = document.querySelectorAll(".delete-student");

students.forEach(student_delete_link => {
    student_delete_link.addEventListener('click', function(e){
        e.preventDefault();
        const href = e.target.href;
        var yes_link = document.getElementById('yes-delete-record-link');
        yes_link.href = href;
        var modal = document.getElementById('modal');
        modal.classList.add('display-modal');
        modal.classList.remove('hide-modal');
    })
});


document.getElementById('no-button').addEventListener('click', function(e){
    e.preventDefault();
    var modal = document.getElementById('modal');
    modal.classList.add('hide-modal');
    modal.classList.remove('display-modal');
    var yes_link = document.getElementById('yes-delete-recird-link');
    yes_link.href = "";
})
