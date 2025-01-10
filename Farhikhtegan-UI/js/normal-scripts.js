function showMessage(text,timeout,class_name){
    const alertDiv = document.createElement('div');

    alertDiv.className = 'alert ' + class_name + ' alert-dismissible fade show';
    alertDiv.role = 'alert';
    alertDiv.style.position = 'fixed';
    alertDiv.style.zIndex = '1051'; // Ensure it appears above the popup
    alertDiv.style.top = '20px';
    alertDiv.style.right = '20px';
    alertDiv.innerHTML = text;
    document.body.appendChild(alertDiv);

    // Remove alert after 3 seconds
    setTimeout(() => {
        alertDiv.classList.remove('show');
        alertDiv.addEventListener('transitionend', () => {
            alertDiv.remove();
        });
    }, timeout);
}

function sendScore(student_id){
    console.log(student_id);
    const score = document.getElementById("score-input-student-"+String(student_id)).value;
    if (score.length === 0) {
        showMessage("! لطفا اول مقدار نمره را وارد کنید", 1300, "alert-warning");
        return;
    }
    console.log(score);
    score.value = "";
    showMessage("! نمره با موفقیت ثبت شد",1300,"alert-success");
}

function sendAttendance(student_id){
    console.log(student_id);
    const attendance = document.getElementById("attendance-checkbox-student-"+String(student_id)).checked;
    console.log(attendance);
    showMessage("! حضور/غیاب با موفقیت ثبت شد",1300,"alert-success");
}