from utility import *
def app():
    # KONU Ekleme ARAYÜZÜ
    st.subheader('Research Submit Form')
    df_staff=pd.read_sql_query("SELECT * from staff_table", the_conn)
    staff_form = st.form(key='staff-form')
    title=staff_form.selectbox(label='Title',options=['Dr.','Assoc.Prof.','Prof.Dr.'])
    Category=staff_form.selectbox(label='Category',options=['CategoryA','CategoryB','CategoryC','CategoryC2','CategoryD','CategoryD1'],key='cat')
    Name=staff_form.text_input(label='Name',value='',key='name')
    Surname=staff_form.text_input(label='Surname',value='',key='surname')
    Orcid_no=staff_form.text_input(label='Orcid No',value='',key='orcid')
    BC_degree = staff_form.text_input(label='BC Degree', value='', key='bcdegre')
    MSc_degree = staff_form.text_input(label='MSc Degree', value='', key='Mscdegre')
    PhD = staff_form.text_input(label='MSc Degree', value='', key='phd')
    Specialized_on=staff_form.text_input(label='Specialized on', value='', key='special')
    Case_study=staff_form.text_input(label='Case Study', value='', key='case')
    Capacity_need=staff_form.multiselect(label='Category',options=['real time measurement','digital process control techniques',
                                                            'visual sensors and environmental applications','data analytics',
                                                            'IT solutions',' IoT applications in environmental management','GIS data modelling',
                                                            'deep learning tecniques','use of ICT infrastructure','use of image processing software','decision support systems'],key='capacity')
    Levelofexperience=staff_form.selectbox(label='Level of experience',options=['basic knowledge','limited experience','intermediate - practical application','advanced'],key='exper')


    konu_rec=(title, Name, Surname, Category, Orcid_no, BC_degree, MSc_degree, PhD, Specialized_on, Case_study, str(Capacity_need), Levelofexperience)
    konu_submit = staff_form.form_submit_button(label='Add')

    if konu_submit:
        if the_conn is not None:
            insert_row(the_conn, konu_rec)
            st.success('Added successfully!')
        else:
            st.error("Error! on database connection .")

    st.dataframe(df_staff)
