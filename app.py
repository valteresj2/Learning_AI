import streamlit as st
from openai import OpenAI







def click_button():
   st.session_state.clicked= True




st.title("Aprendizado Inteligente")




text_input=st.text_input('Escreva aqui qual tema você deseja aprender?')

text_input2=st.text_input('Adicione aqui seu token do OpenAI com o chatgpt 4 liberado.')

if len(text_input2)>0:
    client = OpenAI(
        # This is the default and can be omitted
        api_key=text_input2,
    )




if len(text_input)>0:
   
    st.write('Escolha as sub-áreas do conhecimento que você mais gosta!')
    
    c_exatas = st.multiselect(
    'Escolha as sub-áreas da área de Ciências Exatas e da Terra:',
        ['Matemática','Probabilidade e estatística','Ciência da computação','Astronomia','Física','Química','Geociências','Oceanografia'],
        [], key='exatas')


    
    c_biologica = st.multiselect(
    'Escolha as sub-áreas da área de Ciências Biológicas:',
        ['Genética','Botânica','Zoologia','Ecologia','Morfologia','Fisiologia','Bioquímica','Biofísica','Farmacologia','Imunologia','Microbiologia','Parasitologia'],
        [], key='biologica')


    
    c_engenharias = st.multiselect('Escolha as sub-áreas da área de Engenharias:',
        ['Engenharia civil','Engenharia de minas','Engenharia de materiais e metalúrgica','Engenharia elétrica','Engenharia mecânica','Engenharia química','Engenharia sanitária','Engenharia de produção','Engenharia nuclear','Engenharia de transportes','Engenharia naval e oceânica','Engenharia aeroespacial','Engenharia biomédica'],
        [], key='engenharia')


    
    c_saude =st.multiselect(
    'Escolha as sub-áreas da área da Ciências da Saúde:',
        ['Medicina','Odontologia','Farmácia','Enfermagem','Nutrição','Saúde coletiva','Fonoaudiologia','Fisioterapia e terapia ocupacional','Educação física'],
        [], key='saude')


    c_agraria = st.multiselect(
    'Escolha as sub-áreas da área da Ciências Agrárias:',
        ['Agronomia','Recursos florestais e engenharia florestal','Engenharia agrícola','Zootecnia','Medicina veterinária','Recursos pesqueiros e engenharia de pesca','Ciência e tecnologia de alimentos'],
        [], key='agraria')


    
    c_sociais = st.multiselect(
    'Escolha as sub-áreas da área da Ciências Sociais Aplicadas:',
        ['Direito','Administração','Economia','Arquitetura e urbanismo','Planejamento urbano e regional','Demografia','Ciência da informação','Museologia','Comunicação','Serviço social','Economia doméstica','Desenho industrial','Turismo'],
        [], key='sociais')


    
    c_humanas = st.multiselect(
    'Escolha as sub-áreas da área da Ciências Humanas:',
        ['Filosofia','Sociologia','Antropologia','Arqueologia','História','Geografia','Psicologia','Educação','Ciência política','Teologia'],
        [], key='humanas')


    c_LLA = st.multiselect(
    'Escolha as sub-áreas da área da Linguística, Letras e Artes:',
        ['Linguística','Letras','Artes'],
        [], key='LLA')


    var_ref={'exatas':c_exatas,
             'biologica':c_biologica,
             'engenharias':c_engenharias,
             'saude':c_saude,
             'agraria':c_agraria,
             'sociais':c_sociais,
             'humanas':c_humanas,
             'Linguas':c_LLA
             }
   
###pip install openai --proxy 172.17.21.100:8080
### playht convert voice
#https://docs.play.ht/reference/python-sdk





    prompt=f''' Faça um material em markdown com todos os detalhes no formato de material de aula com o titulo: "{text_input}", 
                e que a escrita desse material seja baseado nas áreas de conhecimentos abaixo, com exemplos e referências da internet:          
                        '''
  
    for i in var_ref:
        if len(var_ref[i])>0:
           materias=', '.join(var_ref[i])
           prompt=prompt+i+': '+materias +' \n'
            



    generated_=st.button("Gerar o Material.", on_click=click_button)

    if generated_:

        chat_completion = client.chat.completions.create(
                        messages=[
                            {
                                "role": "user",
                                "content": prompt,
                            }
                        ],
                        model="gpt-4-0125-preview",
                        temperature=0,
                    )

        st.write(chat_completion.choices[0].message.content)