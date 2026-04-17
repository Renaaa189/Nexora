<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:020617,50:1e1b4b,100:4c1d95&height=220&section=header&text=NEXORA&fontSize=50&fontColor=ffffff&animation=twinkling&fontAlignY=35" />
</p>

## Introducción

**NEXORA** es un chatbot con inteligencia artificial desarrollado en Python que permite mantener conversaciones con un modelo de lenguaje avanzado.  

Funciona como una aplicación web local creada con Streamlit y utiliza la API de Groq para generar respuestas en tiempo real. Está pensado para que cualquier persona pueda usarlo, incluso sin experiencia previa en programación.

La aplicación incluye funciones como creación de nuevos chats, edición de nombres, personalización del usuario con nombre y emoji, y ajustes del comportamiento de la IA como la creatividad de las respuestas o su longitud. Todo esto dentro de una interfaz simple y amigable tipo chat.

---


## Características principales

### Interacción con IA
- Envío de mensajes en tiempo real  
- Procesamiento mediante modelo de lenguaje avanzado  
- Generación de respuestas dinámicas  
- Flujo conversacional continuo  

### Gestión de conversaciones
- Creación de múltiples chats independientes  
- Persistencia del historial durante la sesión  
- Organización de conversaciones por tema  
- Edición de nombres de chats  

### Personalización
- Configuración de nombre de usuario  
- Selección de avatar (emoji)  
- Ajuste de creatividad de respuestas  
- Control de longitud de las respuestas  

### Experiencia de usuario
- Interfaz tipo chat simple y clara  
- Navegación intuitiva  
- Respuestas en tiempo real  
- Uso accesible sin conocimientos técnicos  


---


## <img src="https://media2.giphy.com/media/QssGEmpkyEOhBCb7e1/giphy.gif" width="25"> Tecnologías


<p align="center">
  <img src="https://skillicons.dev/icons?i=python,vscode" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Streamlit-Framework-ff4b4b?style=for-the-badge&logo=streamlit&logoColor=white"/>
  <img src="https://img.shields.io/badge/Groq-API-8e44ad?style=for-the-badge"/>
</p>

<p align="center">
  <sub>
    Python como lenguaje principal • Visual Studio Code como entorno de desarrollo • Streamlit para la interfaz web • Groq para el procesamiento de inteligencia artificial
  </sub>
</p>

---
## Vista del sistema

<table align="center">
  <tr>
    <td align="center">
      <img src="Documentación/Imagenes/NexoraInicio.PNG" width="700" style="border: 3px solid white; border-radius: 10px;"/><br>
      <sub>Pantalla principal del chatbot</sub>
    </td>
  </tr>
</table>

<br>

<table align="center">
  <tr>
    <td align="center">
      <img src="Documentación/Imagenes/NexoraChat.PNG" width="700" style="border: 3px solid white; border-radius: 10px;"/><br>
      <sub>Conversación en tiempo real con Nexora</sub>
    </td>
  </tr>
</table>

<br>

<table align="center">
  <tr>
    <td align="center">
      <img src="Documentación/Imagenes/NexoraChats.PNG" width="250" style="border: 2px solid white; border-radius: 8px;"/><br>
      <sub>Chats</sub>
    </td>
    <td align="center">
      <img src="Documentación/Imagenes/NexoraPerfil.PNG" width="250" style="border: 2px solid white; border-radius: 8px;"/><br>
      <sub>Perfil</sub>
    </td>
    <td align="center">
      <img src="Documentación/Imagenes/NexoraAjustes.PNG" width="250" style="border: 2px solid white; border-radius: 8px;"/><br>
      <sub>Ajustes</sub>
    </td>
  </tr>
</table>

---
---

## [Instalación del proyecto](./Documentación/Nexora%20-%20Documentación.pdf)

<p>Para usar NEXORA necesitás:</p>
<ul>
  <li>Python 3 o superior</li>
  <li>Conexión a internet</li>
</ul>

<pre><code>python --version</code></pre>



### Paso 1: Descargar el proyecto

<pre><code>git clone https://github.com/Renaaa189/Nexora.git
cd Nexora</code></pre>



### Paso 2: Instalar dependencias

<pre><code>pip install -r requirements.txt</code></pre>

<hr>

### Paso 3: Configurar API Key</h3>

<ul>
  <li>Crear cuenta en https://console.groq.com/</li>
  <li>Generar una API Key</li>
</ul>

<p>Crear archivo:</p>

<pre><code>.streamlit/secrets.toml</code></pre>

<p>Agregar:</p>

<pre><code>CLAVE_API = "TU_API_KEY"</code></pre>

<hr>

### Paso 4: Ejecutar la app</h3>

<pre><code>streamlit run chatbot.py</code></pre>

<p>Abrir en el navegador:</p>

<pre><code>http://localhost:8505/</code></pre>

<hr>

