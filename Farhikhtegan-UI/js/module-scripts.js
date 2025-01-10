import {list_of_classes , global_data , homeworks} from "./data.js";

//list classes
export function initializeClassPopup() {
    list_of_classes.forEach(class_details => {
        const class_id = class_details.class_id;
        const class_name = class_details.class_name;
        const number_of_students = class_details.number_of_students;
        const lesson = class_details.lesson;

        const html = `
        <div class="class-card" data-class-id="${class_id}">
            <h2>${class_name}</h2>
            <p><i class="bi bi-book"></i>${lesson}</p>
            <p><i class="bi bi-people"></i> ${number_of_students} دانش آموز</p>
        </div>`;

        document.getElementById("class-list-div").insertAdjacentHTML("beforeend", html);
        const class_card = document.querySelector(`[data-class-id="${class_id}"]`);
        class_card.addEventListener("click", () => {
            showClassDetails(class_id);
        });  
    });
}

function showClassDetails(class_id) {
    const class_details = list_of_classes.find(details => details.class_id===class_id);
    //const class_card = document.querySelector(`[data-class-id="${class_id}"]`);
    const popup = document.getElementById('classPopup');
    const closeButton = popup.querySelector('.close-popup');
    const popup_title = popup.querySelector('#popupTitle');
    const popup_lesson = popup.querySelector('#popupLesson');
    const popup_class = popup.querySelector('#popupClass');
    const popup_student_list = popup.querySelector('.student-list');

    popup_title.textContent = class_details.class_name;
    popup_lesson.textContent = class_details.lesson;
    popup_class.textContent = class_details.class_name;

    //reset students list
    popup_student_list.innerHTML = "";

    class_details.students.forEach(student => {
        const additional_data = `
        <div class="student-item" style="direction: rtl;" data-student-id=${student.user_id}>
            <div class="student-info">
            <span class="student-name"><b>نام و نام خانوادگی : </b> ${student.name}</span>
            <span class="student-id"><b>رشته : </b> ${student.subject}</span>
            <div class="form-check">
                <p><b>حاضر در کلاس : </b> <input class="form-check-input" type="checkbox" value="" id="attendance-checkbox-student-${student.user_id}"></p>
            </div>
            <div>
                <input type="number" step="0.01" class="form-control" placeholder="نمره" aria-label="نمره" aria-describedby="basic-addon2" id="score-input-student-${student.user_id}">
            </div>
            <div style="display: flex;gap: 5px;margin-top: 5px;">
                <button type="button" class="btn btn-primary btn-sm" onclick="sendScore(${student.user_id})">ثبت نمره</button>
                <button type="button" class="btn btn-primary btn-sm" onclick="sendAttendance(${student.user_id})">ثبت حضورت عیاب</button>
            </div>
            </div><hr>
        </div>
        `;

        popup_student_list.insertAdjacentHTML("beforeend", additional_data);

        //input limiter
        const scoreInput = document.getElementById(`score-input-student-${student.user_id}`);
        scoreInput.addEventListener('input', (number) => {
            if (number.target.value > 20) {
                showMessage("مقدار نمره نمیتواند بالاتر از 20 باشد",1150,'alert-warning');
            number.target.value = 20;
        }

        // Set input type to number for numeric keyboard
        scoreInput.setAttribute('inputmode', 'numeric');
        
        });

    });
    
    closeButton.addEventListener('click', () => {
        popup.classList.remove('active');
    });
    
    // Close popup when clicking outside
    popup.addEventListener('click', (e) => {
        if (e.target === popup) {
            popup.classList.remove('active');
        }
    });

    //open popup
    popup.classList.add("active");
}

export function ShowProfileDropdownDatas() {
    if (global_data.is_teacher===true) {
        const first_name = global_data.fist_name;
        const last_name = global_data.last_name;
        const age = global_data.age;
        const national_code = global_data.national_code;
        const lessons = global_data.lessons;
        const html = `
        <div class="user-info" id="user-info-dropdown">
            <p><strong>نام:</strong> <span id="firstName">${first_name}</span></p>
            <p><strong>نام خانوادگی:</strong> <span id="lastName">${last_name}</span></p>
            <p><strong>سن:</strong> <span id="userAge">${age}</span></p>
            <p><strong>کد ملی:</strong> <span id="nationalCode">${national_code}</span></p>
            <p><strong>دروس:</strong> <span id="teacherLessons">${lessons}</span></p>
        </div>`;
        document.getElementById("dropdown-content-div").insertAdjacentHTML("afterbegin",html);
    }else{
        const first_name = global_data.fist_name;
        const last_name = global_data.last_name;
        const age = global_data.age;
        const national_code = global_data.national_code;
        const grade = global_data.grade;
        const subject = global_data.subject;
        const school_class = global_data.school_class;
        const html = `
        <div class="user-info" id="user-info-dropdown">
            <p><strong>نام:</strong> <span id="firstName">${first_name}</span></p>
            <p><strong>نام خانوادگی:</strong> <span id="lastName">${last_name}</span></p>
            <p><strong>سن:</strong> <span id="userAge">${age}</span></p>
            <p><strong>کد ملی:</strong> <span id="nationalCode">${national_code}</span></p>
            <p><strong>پایه:</strong> <span id="userGrade">${grade}</span></p>
            <p><strong>رشته:</strong> <span id="userSubject">${subject}</span></p>
            <p><strong>کلاس:</strong> <span id="userClass">${school_class}</span></p>
        </div>`;
        document.getElementById("dropdown-content-div").insertAdjacentHTML("afterbegin",html);
    }
}

export function initializeHomeworks() {
    const cards_div_html = `
    <div class="container py-5" style="direction: rtl;" >

        <header class="mb-4">
            <h1 class="display-5 mb-3">
                <i class="bi bi-calendar-week text-primary"></i>
                تکالیف فردا
            </h1>
        </header>

        <div class="row g-4" id="homework-cards-div"></div>

    </div>`;

    document.getElementById("class-list-div").insertAdjacentHTML("beforeend",cards_div_html);
    if (homeworks.length === 0) {
        const noHomeworkHtml = `
        <div class="empty-state">
            <div class="icon-wrapper">
                <svg class="icon" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <rect width="8" height="4" x="8" y="2" rx="1" ry="1"/><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"/><path d="M12 11h4"/><path d="M12 16h4"/><path d="M8 11h.01"/><path d="M8 16h.01"/>
                </svg>
            </div>
            <h3 class="title">هیچ تکلیفی برای فردا ثبت نشده است !!</h3>
        </div>`;
        document.getElementById("homework-cards-div").insertAdjacentHTML("beforeend", noHomeworkHtml);
    } else {
        homeworks.forEach(homework_details => {
            const card_html = `
            <div class="col-md-6" id="homework-card-${homework_details.homework_id}">
                <div class="card h-100 shadow-sm">
                    <div class="card-body">
                        <div class="d-flex justify-content-between align-items-center mb-3">
                            <h2 class="h4 mb-0">${homework_details.homework_for}</h2>
                        </div>
                        <div class="homework-section">
                            <h3 class="h6 text-danger mb-2">
                                <i class="bi bi-journal-text"></i>
                                توضیحات
                            </h3>
                            <p class="mb-1">${homework_details.homework_description}</p>
                            <small class="text-muted">مهلت : ${homework_details.homework_expiration_date}</small>
                        </div>
                    </div>
                </div>
            </div>`;
            document.getElementById("homework-cards-div").insertAdjacentHTML("beforeend",card_html);
        });
    }
}