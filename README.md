# 📄 Generador de CV en LaTeX

Un generador automático de CV profesional que convierte datos en formato JSON a elegantes documentos PDF usando LaTeX.

## 🚀 Características

- **Dos versiones**: CV físico (para impresión) y CV online (con enlaces clicables)
- **Formato JSON**: Datos estructurados y fáciles de editar
- **Compilación automática**: Genera PDF directamente desde Python
- **Plantillas profesionales**: Diseño limpio y moderno
- **Limpieza automática**: Elimina archivos temporales después de la compilación

## 📋 Requisitos

### Dependencias del sistema
```bash
# Ubuntu/Debian
sudo apt install texlive-latex-recommended texlive-latex-extra
```

## 🔧 Uso básico

### 1. Preparar tus datos

Crea un archivo JSON con tus datos personales. Puedes usar `cv_ejemplo.json` como referencia:

```json
{
    "nombre": "Tu Nombre Completo",
    "ciudad": "Tu Ciudad",
    "pais": "Tu País",
    "telefono": "+XX XXX XXX XXX",
    "correo": "tu.email@dominio.com",
    "linkedin": "linkedin.com/in/tu-perfil",
    "resumen": "Breve descripción profesional...",
    "experiencia": [
        {
            "empresa": "Nombre de la Empresa",
            "ciudad": "Ciudad",
            "puesto": "Tu Puesto",
            "fechas": "Mes Año -- Presente",
            "logros": [
                "Logro 1 con métricas específicas",
                "Logro 2 con resultados cuantificables",
                "Logro 3 con impacto demostrable"
            ]
        }
    ],
    "formacion": [
        {
            "titulo": "Título del Grado/Máster",
            "centro": "Universidad/Instituto",
            "fechas": "Año -- Año"
        }
    ],
    "habilidades": [
        "Habilidad técnica 1",
        "Habilidad técnica 2",
        "Habilidad técnica 3"
    ]
}
```

### 2. Generar tu CV

#### Opción 1: Con archivo por defecto
```bash
python3 main.py
```
*Usa `cv.json` como archivo de datos*

#### Opción 2: Con archivo personalizado
```bash
python3 main.py mi_cv.json
```
*Usa el archivo JSON que especifiques*

### 3. Resultados

El script generará dos archivos PDF:
- `cv_fisico.pdf` - Versión optimizada para impresión
- `cv_online.pdf` - Versión con enlaces clicables

## 📝 Personalización

### Modificar plantillas

Puedes editar las plantillas LaTeX para cambiar el diseño:

- `template.tex` - Plantilla para CV físico
- `template_online.tex` - Plantilla para CV online

### Añadir nuevos campos

Para añadir campos adicionales:

1. Añade el campo en tu archivo JSON
2. Actualiza la función correspondiente en `main.py`
3. Modifica las plantillas LaTeX para incluir el nuevo campo

## 🔍 Ejemplo de ejecución

```bash
$ python3 main.py cv_ejemplo.json

🚀 Generando tu CV...
==================================================
📋 Usando archivo de datos: cv_ejemplo.json
📄 Generando cv_fisico...
✅ Archivo LaTeX generado: cv_fisico.tex
✅ PDF generado: cv_fisico.pdf
✅ Archivo temporal eliminado: cv_fisico.tex

--------------------------------------------------

📄 Generando cv_online...
✅ Archivo LaTeX generado: cv_online.tex
✅ PDF generado: cv_online.pdf
✅ Archivo temporal eliminado: cv_online.tex

==================================================
📋 RESUMEN:
✅ CVs generados exitosamente: 2/2
🎉 ¡Ambos CVs generados correctamente!
📄 cv_fisico.pdf - Versión para impresión
🌐 cv_online.pdf - Versión online
==================================================
```

## 💡 Consejos

1. **Usa métricas**: Incluye números y porcentajes en tus logros
2. **Sé específico**: Detalla tecnologías y herramientas concretas
3. **Actualiza regularmente**: Mantén tu CV siempre al día
4. **Revisa ortografía**: Usa un corrector antes de generar el PDF
5. **Adapta el contenido**: Personaliza para cada oportunidad laboral

## 🤝 Contribuciones

¿Tienes ideas para mejorar el generador? ¡Las contribuciones son bienvenidas!

1. Haz un fork del proyecto
2. Crea una rama para tu feature
3. Realiza tus cambios
4. Envía un pull request
