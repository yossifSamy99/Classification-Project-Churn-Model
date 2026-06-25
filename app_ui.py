import streamlit as st
import pandas as pd

# استيراد الأدوات الخاصة بك
from utils.inference import predict_new
from utils.CustomerData import CustomerData
from utils.config import APP_NAME, VERSION, SECRET_KEY_TOKEN, preprocessor, RandomForestTuned, xgb_tuned

# 1. إعداد الصفحة والعنوان
st.set_page_config(page_title=APP_NAME, layout="centered")
st.title(f"{APP_NAME} v{VERSION}")
st.write(f"مرحباً بك في الواجهة الرسومية لتطبيق {APP_NAME}")


# 2. نظام التحقق (API Key) في الشريط الجانبي
st.sidebar.header("التحقق من الهوية")
api_key = st.sidebar.text_input("أدخل مفتاح الـ X-API-Key", type="password")

if not api_key:
    st.info("من فضلك أدخل الـ API Key في الشريط الجانبي لتتمكن من استخدام التطبيق.")
    st.stop()

if api_key != SECRET_KEY_TOKEN:
    st.error("❌ خطأ 403: غير مصرح لك بالدخول. الـ API Key غير صحيح.")
    st.stop()

st.sidebar.success("🔑 تم التحقق بنجاح")


# 3. اختيار النموذج (Model)
st.sidebar.header("إعدادات النموذج")
model_choice = st.sidebar.selectbox(
    "اختر النموذج المراد استخدامه للتوقع:",
    ["Random Forest", "XGBoost"]
)


# 4. استمارة إدخال بيانات العميل (Form)
st.header("إدخال بيانات العميل")
st.write("قم بملء البيانات التالية بدقة:")

with st.form("customer_data_form"):
    
    col1, col2 = st.columns(2)
    
    with col1:
        CreditScore = st.number_input("الرصيد الائتماني (Credit Score)", min_value=0, value=600)
        Geography = st.selectbox("الدولة (Geography)", ['France', 'Spain', 'Germany'])
        Gender = st.selectbox("الجنس (Gender)", ['Female', 'Male'])
        Age = st.number_input("العمر (Age)", min_value=18, max_value=100, value=35)
        Tenure = st.number_input("عدد سنوات التعامل (Tenure)", min_value=0, max_value=10, value=5)
        
    with col2:
        Balance = st.number_input("الحساب البنكي (Balance)", min_value=0.0, value=0.0, step=100.0)
        NumOfProducts = st.number_input("عدد المنتجات المشترك بها (NumOfProducts)", min_value=1, max_value=4, value=1)
        HasCrCard = st.selectbox("هل يمتلك بطاقة ائتمان؟ (HasCrCard)", options=[1, 0], format_func=lambda x: "Yes [1]" if x == 1 else "No [0]")
        IsActiveMember = st.selectbox("هل هو عضو نشط؟ (IsActiveMember)", options=[1, 0], format_func=lambda x: "Yes [1]" if x == 1 else "No [0]")
        EstimatedSalary = st.number_input("الراتب المتوقع (EstimatedSalary)", min_value=0.0, value=50000.0, step=500.0)

    # زر إرسال البيانات للتوقع
    submit_button = st.form_submit_button(label="بدء التوقع (Predict)")


# 5. معالجة البيانات وإظهار النتيجة
if submit_button:
    try:
        # بناء كائن البيانات مطابفاً تماماً للـ Pydantic Model الخاص بك
        data = CustomerData(
            CreditScore=CreditScore,
            Geography=Geography,
            Gender=Gender,
            Age=Age,
            Tenure=Tenure,
            Balance=Balance,
            NumOfProducts=NumOfProducts,
            HasCrCard=HasCrCard,
            IsActiveMember=IsActiveMember,
            EstimatedSalary=EstimatedSalary
        )
    except Exception as e:
        st.error(f"خطأ في تجميع البيانات: {e}")
        st.stop()

    # تحديد الموديل بناءً على اختيار المستخدم
    selected_model = RandomForestTuned if model_choice == "Random Forest" else xgb_tuned
    
    st.write("### نتيجة التوقع:")
    with st.spinner(f"جاري حساب التوقع باستخدام {model_choice}..."):
        try:
            # تشغيل ميثود التوقع الخاصة بك
            result = predict_new(data=data, preprocessor=preprocessor, model=selected_model)
            
            # إظهار النتيجة للمستخدم بنجاح
            st.success("تم التوقع بنجاح!")
            st.json(result)
            
        except Exception as e:
            st.error(f"❌ خطأ 500 internal server error: حدثت مشكلة أثناء تشغيل النموذج.")
            st.exception(e)