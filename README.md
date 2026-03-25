# CORPOSALUD-MAQUETA

## 1\. Descripción y Propósito

**PAS** es una herramienta de grado profesional diseñada para la extracción automatizada de datos desde comprobantes salariales (maquetas) en formato PDF o imagen.

El propósito principal es eliminar la carga administrativa de transcripción manual, transformando documentos no estructurados en reportes de Excel organizados. Está optimizado para ejecutarse en hardware de recursos limitados, priorizando la velocidad de procesamiento y la modularidad del código.

## 2\. Estructura de Carpetas (Modular)

Diseñada para separar las responsabilidades (Separation of Concerns):

```text
payroll_automation/
├── config/                 # Configuraciones externas
│   ├── settings.json       # Rutas y parámetros del OCR
│   └── mapping.json        # Diccionario de palabras clave/campos
├── data/
│   ├── input/              # PDFs a procesar
│   ├── output/             # Excels individuales y consolidados
│   └── temp/               # Imágenes temporales (pre-procesamiento)
├── src/
│   ├── core/               # Lógica de negocio e interfaces
│   │   ├── base_extractor.py
│   │   └── processor.py
│   ├── extractors/         # Implementaciones de OCR (Tesseract)
│   │   └── tesseract_handler.py
│   ├── models/             # Clases de datos (Entidades)
│   │   └── salary_record.py
│   ├── utils/              # Herramientas de apoyo
│   │   ├── excel_helper.py
│   │   └── config_loader.py
│   └── ui/                 # Interfaz de usuario ligera
│       └── app_gui.py
├── main.py                 # Punto de entrada único
├── requirements.txt        # Dependencias
└── README.md
```

## 3\. Librerías y Tutorial de Instalación

### Librerías Utilizadas

  * **`pytesseract`**: Interfaz para el motor Tesseract OCR (ligero y rápido).
  * **`pdf2image`**: Convierte páginas de PDF a objetos de imagen.
  * **`pandas`**: Estructuración y limpieza de los datos salariales.
  * **`openpyxl`**: Motor para la creación de archivos `.xlsx`.
  * **`Pillow` (PIL)**: Manipulación básica de imágenes.
  * **`CustomTkinter`**: Interfaz gráfica moderna y de bajo consumo.

### Tutorial de Instalación

1.  **Clonar el repositorio** (o crear la carpeta del proyecto).
2.  **Instalar Tesseract OCR** (Motor externo):
      * Descarga el instalador para Windows (ej. v5.x) desde [UB Mannheim](https://www.google.com/search?q=https://github.com/UB-Mannheim/tesseract/wiki).
      * **Importante:** Anota la ruta de instalación (ej. `C:\Program Files\Tesseract-OCR\tesseract.exe`).
3.  **Instalar poppler** (Necesario para `pdf2image`):
      * Descarga los binarios de Poppler y agrega la carpeta `bin` a las variables de entorno (PATH) de Windows.
4.  **Instalar dependencias de Python**:
    ```bash
    pip install pytesseract pdf2image pandas openpyxl customtkinter
    ```

## 4\. Diagrama de Clases (Arquitectura)

Para cumplir con el **Patrón Strategy** y **SOLID**, utilizaremos la siguiente jerarquía:

  * **`BaseExtractor` (Interface):** Define el método `extract_text()`.
  * **`TesseractExtractor` (Concrete Strategy):** Implementa la extracción usando Tesseract.
  * **`SalaryProcessor` (Context):** Orquestador que recibe los archivos y utiliza el extractor.
  * **`SalaryRecord` (Model):** Clase que representa una fila de la maqueta (Nombre, Monto, etc.).

## 5\. Consideraciones Adicionales

### Manejo de Configuraciones (`JSON`)

Para evitar el "Hardcoding" (escribir rutas directamente en el código), usaremos un archivo `config/settings.json`. Esto permite que si el usuario instala Tesseract en otra carpeta, solo deba cambiar el JSON y no el código fuente.

### Principio DRY en Excel

El `ExcelHelper` tendrá un método estático `save_to_excel(data, filename, append=False)`. Este mismo método servirá tanto para crear el Excel individual (paso 3 del flujo) como para alimentar el consolidado final (paso 4).

### Limpieza de Temporales

Dado que transformaremos PDF a Imágenes para el OCR, el sistema incluirá un módulo de limpieza automática que borra la carpeta `data/temp/` al finalizar cada ejecución, manteniendo el disco limpio.

