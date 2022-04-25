# %%
import pandas as pd
import streamlit as st
from collections import Counter
from PIL import Image

# %%
im = Image.open("./logo_ugry.png")
st.set_page_config(page_title="Отклики на задачи", page_icon=im)

# %%
st.title("Распределение типов связи")
st.write("Выбранные типы связи для задач. Датафрейм был отфильтрован, учитываются только следующие платформы: iOS, Android")


uploaded_file = st.file_uploader("Выбирете файл")


if uploaded_file is not None:
     df = pd.read_csv(uploaded_file, sep='|')
     df.columns = [
        'task_id',
        'task_name',
        'status',
        'communication_method',
        'date_creation',
        'customer_phone',
        'platform',
        'number_responses',
        'number_matches',
        'number_prematches'
     ]

     df_platform_admins = df[df['platform'] == 'admins']
     df_platform_ios = df[df['platform'] == 'ios']
     df_platform_android = df[df['platform'] == 'android']

     # удаление пропусков, которые появляются из за особенностей выгрузки
     df = df.dropna()

     file_container = st.expander("Check your uploaded .csv")   
     st.write(df)
else:
    st.info(
        f"""
             👆 Загрузите файл с расширением csv. В файле должны стого содержаться следующие столбцы:
             - id задачи
             - Название	задачи
             - Статус
             - Способ связи
             - Дата создания
             - Телефон заказчика
             - Платформа
             - Кол-во откликов
             - Кол-во матчей
             - Кол-во прематчей
             """
    )
    st.stop()

# %%
st.write("# Количество задач, у которых есть хотя бы один отклик, процент таких задач")

# %%
st.write("## Admins")

# %%
one_response_admins = df_platform_admins[df_platform_admins['number_responses'] >= 1].count()[0]
st.write('Количество задач, у который есть хотя бы один отклик:', one_response_admins)

# %%
total_number_tasks_admins = df_platform_admins['task_id'].nunique()
st.write('Общее количетсво задач:', total_number_tasks_admins)

# %%
st.write('Процент задач, у которых есть хотя бы один отклик = {:.0f}%'
      .format(one_response_admins * 100 / total_number_tasks_admins))

# %%
st.write("## iOS")

# %%
one_response_ios = df_platform_ios[df_platform_ios['number_responses'] >= 1].count()[0]
st.write('Количество задач, у который есть хотя бы один отклик:', one_response_ios)

# %%
total_number_tasks_ios = df_platform_ios['task_id'].nunique()
st.write('Общее количетсво задач:', total_number_tasks_ios)

# %%
st.write('Процент задач, у которых есть хотя бы один отклик = {:.0f}%'
      .format(one_response_ios * 100 / total_number_tasks_ios))

# %%
st.write("## Android")

# %%
one_response_android = df_platform_android[df_platform_android['number_responses'] >= 1].count()[0]
st.write('Количество задач, у который есть хотя бы один отклик:', one_response_android)

# %%
total_number_tasks_android = df_platform_android['task_id'].nunique()
st.write('Общее количетсво задач:', total_number_tasks_android)

# %%
st.write('Процент задач, у которых есть хотя бы один отклик = {:.0f}%'
      .format(one_response_android * 100 / total_number_tasks_android))

# %%

st.write("# Сколько откликов получает задача")

# %%
st.write("## Admins")

# %%
st.write(Counter(df_platform_admins['number_responses']))

# %%
st.write("## iOS")

# %%
st.write(Counter(df_platform_ios['number_responses']))

# %%
st.write("## Android")

# %%
st.write(Counter(df_platform_android['number_responses']))

# %%
st.write("Общее распределение откликов")

# %%
st.write(Counter(df['number_responses']))


