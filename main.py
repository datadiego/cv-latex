import os
import json
import subprocess
import sys

def render_experiencia(exp_list):
    """Renderiza la sección de experiencia laboral"""
    result = []
    for exp in exp_list:
        # Línea 1: Empresa y Ciudad
        result.append("\\begin{tabular*}{\\textwidth}{@{}l@{\\extracolsep{\\fill}}r@{}}")
        result.append(f"\\textbf{{{exp['empresa']}}} & \\textbf{{{exp['ciudad']}}} \\\\")
        result.append("\\end{tabular*}")

        # Línea 2: Puesto y Fechas
        result.append("\\begin{tabular*}{\\textwidth}{@{}l@{\\extracolsep{\\fill}}r@{}}")
        result.append(f"\\textit{{{exp['puesto']}}} & \\textit{{{exp['fechas']}}} \\\\")
        result.append("\\end{tabular*}")

        # Lista de logros
        result.append("\\begin{itemize}[leftmargin=*]")
        for logro in exp['logros']:
            result.append(f"  \\item {logro}")
        result.append("\\end{itemize}")

        # Espacio extra entre bloques
        result.append("\\vspace{6pt}\n")

    return "\n".join(result)

def render_formacion(formacion_list):
    """Renderiza la sección de formación académica"""
    result = []
    for form in formacion_list:
        result.append(f"\\textbf{{{form['titulo']}}} ({form['centro']}) \\hfill {form['fechas']}\\\\")
    return "\n".join(result)

def render_habilidades(hab_list):
    """Renderiza la sección de habilidades"""
    return "\n".join([f"  \\item {hab}" for hab in hab_list])

def generar_cv(template_file, output_name, json_file="cv.json"):
    """Genera un CV usando el template especificado"""
    print(f"📄 Generando {output_name}...")
    
    # Línea decorativa
    linea = r"\noindent\textcolor{gray}{\rule{\textwidth}{0.4pt}}\vspace{6pt}"

    # Cargar datos del JSON
    with open(json_file, encoding="utf-8") as f:
        datos = json.load(f)

    # Cargar template
    with open(template_file, encoding="utf-8") as f:
        template = f.read()

    # Generar contenido LaTeX
    tex = template.format(
        nombre=datos["nombre"],
        ciudad=datos["ciudad"],
        pais=datos["pais"],
        telefono=datos["telefono"],
        correo=datos["correo"],
        linkedin=datos["linkedin"],
        resumen=datos["resumen"],
        experiencia=render_experiencia(datos["experiencia"]),
        formacion=render_formacion(datos["formacion"]),
        habilidades=render_habilidades(datos["habilidades"]),
        linea=linea,
    )

    # Escribir archivo temporal .tex
    tex_file = f"{output_name}.tex"
    with open(tex_file, "w", encoding="utf-8") as f:
        f.write(tex)

    print(f"✅ Archivo LaTeX generado: {tex_file}")
    
    # Compilar a PDF
    try:
        result = subprocess.run(
            ["pdflatex", "-interaction=nonstopmode", tex_file],
            capture_output=True,
            text=True,
            check=True
        )
        print(f"✅ PDF generado: {output_name}.pdf")
        
        # Limpiar archivos auxiliares
        extensions_to_remove = ['.aux', '.log', '.out', '.fls', '.fdb_latexmk']
        for ext in extensions_to_remove:
            aux_file = f"{output_name}{ext}"
            if os.path.exists(aux_file):
                os.remove(aux_file)
        
        # Eliminar archivo .tex temporal
        if os.path.exists(tex_file):
            os.remove(tex_file)
            print(f"✅ Archivo temporal eliminado: {tex_file}")
            
    except subprocess.CalledProcessError as e:
        print(f"❌ Error al compilar {tex_file}:")
        print(e.stderr)
        return False
    except FileNotFoundError:
        print("❌ Error: pdflatex no está instalado o no está en el PATH")
        print("Instálalo con: sudo apt install texlive-latex-recommended texlive-latex-extra")
        return False
    
    return True

def main():
    """Función principal que genera ambos CVs"""
    print("🚀 Generando tu CV...")
    print("=" * 50)
    
    # Verificar argumentos de línea de comandos
    json_file = "cv.json"
    if len(sys.argv) > 1:
        json_file = sys.argv[1]
        print(f"📋 Usando archivo de datos: {json_file}")
    
    # Verificar que existan los archivos necesarios
    required_files = [json_file, "template.tex", "template_online.tex"]
    for file in required_files:
        if not os.path.exists(file):
            print(f"❌ Error: No se encontró el archivo {file}, puedes adjuntarlo con python3 main.py <archivo_json>")
            sys.exit(1)
    
    success_count = 0
    
    # Generar CV físico
    if generar_cv("template.tex", "cv_fisico", json_file):
        success_count += 1
    
    print("\n" + "-" * 50 + "\n")
    
    # Generar CV online
    if generar_cv("template_online.tex", "cv_online", json_file):
        success_count += 1
    
    # Resumen final
    print("\n" + "=" * 50)
    print("📋 RESUMEN:")
    print(f"✅ CVs generados exitosamente: {success_count}/2")
    
    if success_count == 2:
        print("🎉 ¡Ambos CVs generados correctamente!")
        print("📄 cv_fisico.pdf - Versión para impresión")
        print("🌐 cv_online.pdf - Versión online")
    elif success_count == 1:
        print("⚠️  Solo se generó un CV correctamente. Revisa los errores anteriores.")
    else:
        print("❌ No se pudo generar ningún CV. Revisa los errores anteriores.")
    
    print("=" * 50)

if __name__ == "__main__":
    main()
