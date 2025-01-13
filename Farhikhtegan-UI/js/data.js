export const global_data = {
    user_id:2,
    is_teacher:true,
    username:1452381459,
    fist_name:"صمد",
    last_name:"مرادی",
    age:34,
    national_code:1452381459,
    lessons:['ریاضی','فیزیک'],
    subject:"تجربی",
    grade:"دهم",
    school_class:"دهم ریاضی تجربی"
};

export const homeworks = [
    {
        homework_id:14,
        homework_for:"فیزیک",
        homework_description:"تمرین صفحه 12 و 13 در دفتر بررسی خواهد شد",
        homework_expiration_date:"1403/10/20"
    },
    {
        homework_id:12,
        homework_for:"ریاضی",
        homework_description:"امتحان از مثلثات بجر توابع مثلثاتی",
        homework_expiration_date:"1403/10/20"
    },
    {
        homework_id:20,
        homework_for:"امادگی",
        homework_description:"پرسش درس 6",
        homework_expiration_date:"1403/10/20"
    },
];

export const list_of_classes = [
    {
        "class_name":"دهم ریاضی",
        "class_id":2,
        "number_of_students":11,
        "lesson":"هندسه",
        "students":[
            {"name":"دانیال خانی","user_id":1,"subject":"ریاضی"},
            {"name":"حسین عبدی","user_id":5,"subject":"ریاضی"},
        ]
    },
    {
        "class_name":"دهم ریاضی و تجربی",
        "class_id":1,
        "number_of_students":20,
        "lesson":"ریاضی",
        "students":[
            {"name":"دانیال خانی","user_id":1,"subject":"ریاضی"},
            {"name":"بهرام قدیم قبادی","user_id":3,"subject":"تجربی"},
        ]
    }
];