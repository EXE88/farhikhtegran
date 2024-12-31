import {list_of_classes , global_data} from "./data.js";

//list classes
export function initializeClassPopup() {
    if (global_data.is_teacher === true) {
        list_of_classes.forEach(class_details => {
            const class_id = class_details.class_id;
            const class_name = class_details.class_name;
            const number_of_students = class_details.number_of_students;
            const lesson = class_details.lesson;

            const html = `
            <div class="class-card" data-class-id="${class_id}">
                <h2>${class_name}</h2>
                <p><i class="bi bi-book"></i> ${lesson}</p>
                <p><i class="bi bi-people"></i> ${number_of_students} دانش آموز</p>
            </div>`;

            document.getElementById("class-list-div").insertAdjacentHTML("beforeend", html);

            const class_card = document.querySelector(`[data-class-id="${class_id}"]`);
            class_card.addEventListener("click", () => {
                showClassDetails(class_id);
            });
        });
    }
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
                    <p>حاضر است : <input class="form-check-input" type="checkbox" value="" id="attendanceCheck"></p>
                </div>
                <div>
                    <input type="number" step="0.01" class="form-control" placeholder="نمره" aria-label="نمره" aria-describedby="basic-addon2">
                </div>
                <div style="display: flex;gap: 5px;margin-top: 5px;">
                    <button type="button" class="btn btn-primary btn-sm">ثبت نمره</button>
                    <button type="button" class="btn btn-primary btn-sm">ثبت حضورت عیاب</button>
                </div>
            </div><hr>
        </div>
        `;
        popup_student_list.insertAdjacentHTML("beforeend",additional_data);
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