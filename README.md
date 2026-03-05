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

