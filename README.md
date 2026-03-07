# Organizador de Arquivos

Um aplicativo com interface gráfica para organizar automaticamente arquivos em pastas de acordo com suas extensões.

## Funcionalidades

- Interface com **CustomTkinter**
- **Dark Mode e Light Mode** - Detecta automaticamente a preferência do sistema
- Organiza arquivos em categorias:
  - **Imagens**: `.jpg, .jpeg, .png, .gif, .bmp, .webp, .svg, .ico`
  - **Documentos**: `.pdf, .doc, .docx, .txt, .xlsx, .xls, .pptx, .ppt, .csv`
  - **Vídeos**: `.mp4, .mkv, .avi, .mov, .wmv, .flv, .webm, .m4v`
  - **Áudio**: `.mp3, .wav, .flac, .aac, .wma, .m4a, .ogg, .opus`
  - **Arquivos**: `.zip, .rar, .7z, .tar, .gz, .iso`
  - **Código**: `.py, .java, .js, .ts, .cpp, .c, .html, .css, .json, .xml`
  - **Executáveis**: `.exe, .msi, .dmg, .app`
  - **Outros**: Qualquer extensão não catalogada
- Visualização da estrutura atual da pasta
- Tratamento de conflitos de nomes de arquivo
- Log detalhado das operações realizadas

## Recursos Principais

- **Tema Automático**: Detecta automaticamente o tema escuro/claro do sistema operacional
- **Manejo de Duplicatas**: Se um arquivo com o mesmo nome já existe, adiciona um sufixo
- **Log Detalhado**: Mostra exatamente quais arquivos foram movidos
- **Interface Responsiva**: Redimensionável e adaptável

## Customização

Para adicionar novas categorias ou extensões, edite o arquivo `config.py`:

```python
FILE_CATEGORIES = {
    "Sua Categoria": [".ext1", ".ext2", ".ext3"],
    # ... outras categorias
}
```

## ⚠️ Observações Importantes

- A organização é **permanente** - os arquivos serão realmente movidos
- Arquivos ocultos (começando com `.`) são ignorados
- Se ocorrer erro ao mover um arquivo, ele não será processado

## Imagens Funcionamento

Antes da execução
<img width="1486" height="790" alt="image" src="https://github.com/user-attachments/assets/6e9032e8-bc0c-4bc1-b9c5-b0fe066b04af" />

Despois da execução

<img width="1486" height="790" alt="depois" src="https://github.com/user-attachments/assets/cdd65238-2b4a-48cd-920e-9a9c3c5ec5f0" />

Programa

<img width="846" height="752" alt="foto2" src="https://github.com/user-attachments/assets/bbc2b0fb-a074-402d-9641-89800bbddeb6" />

