// Mock data for demonstration
const classData = {
    math101: {
        title: 'دهم ریاضی تجربی',
        professor: 'بهنام مددی',
        lessons: ['ریاضی','هندسه'],
        room: 'دهم تجربی ریاضی',
        students_number: 30,
        students: [
            { subject: 'ریاضی', name: 'دانیال خانی' },
            { subject: 'تجربی', name: 'بهرام قدیم قبادی' },
            { subject: 'تجربی', name: 'امیرعلی شوفری' },
            { subject: 'ریاضی', name: 'اردا نظری' },
            { subject: 'تجربی', name: 'محمد مهدی صمدی' },
            { subject: 'ریاضی', name: 'حسین عبدی' },      
        ]
    },
    phys201: {
        title: 'دهم انسانی',
        professor: 'صمد صمدی',
        lessons: 'فیزیک',
        room: 'دهم انسانی',
        students_number: 25,
        students: [
            { subject: 'ریاضی', name: 'صمدی' },
            { subject: 'ریاضی', name: 'صمدی' },
            { subject: 'ریاضی', name: 'صمدی' },
        ]
    },
    chemestry: {
        title: 'دوازدهم انسانی',
        professor: 'صمد صمدی',
        lessons: 'شیمی',
        room: 'دوازدهم انسانی',
        students_number: 9,
        students: [
            { subject: 'ریاضی', name: 'صمدی' },
            { subject: 'ریاضی', name: 'صمدی' },
            { subject: 'ریاضی', name: 'صمدی' },
        ]
    }    
};

export function initializeClassPopup() {
    try {
        Object.keys(classData).forEach(key => {
            const data = `        
            <div class="class-card" data-class-id="${key}">
            <h2>${classData[key].title}</h2>
            <p><i class="bi bi-book"></i>${classData[key].lessons}</p>
            <p><i class="bi bi-people"></i> ${classData[key].students_number} دانش اموز</p>
            </div>`;
        document.getElementById("class-list-div").insertAdjacentHTML("beforeend",data)
        });
    } 
    catch (error) {
        console.log(error)
    }
    const popup = document.getElementById('classPopup');
    const closeButton = popup.querySelector('.close-popup');
    const classCards = document.querySelectorAll('.class-card');

    // Close popup when clicking the close button
    closeButton.addEventListener('click', () => {
        popup.classList.remove('active');
    });

    // Close popup when clicking outside
    popup.addEventListener('click', (e) => {
        if (e.target === popup) {
            popup.classList.remove('active');
        }
    });

    // Handle class card clicks
    classCards.forEach(card => {
        card.addEventListener('click', () => {
            const classId = card.getAttribute('data-class-id');
            showClassDetails(classId);
        });
    });

}

function showClassDetails(classId) {
    const data = classData[classId];
    if (!data) return;

    // Update popup content
    document.getElementById('popupTitle').textContent = data.title;
    document.getElementById('popupProfessor').textContent = data.professor;
    document.getElementById('popupLessons').textContent = data.lessons;
    document.getElementById('popupRoom').textContent = data.room;

    // Update student list
    const studentList = document.querySelector('.student-list');
    studentList.innerHTML = data.students.map(student => `
        <div class="student-item" style="direction: rtl;">
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
    `).join('');

    // Show popup
    document.getElementById('classPopup').classList.add('active');
}