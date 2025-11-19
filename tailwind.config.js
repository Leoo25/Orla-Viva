/** @type {import('tailwindcss').Config} */
module.exports = {
  // AQUI ESTAVA O PROBLEMA: O Tailwind precisa saber onde ler o HTML
  content: [
      // Procura em todos os arquivos HTML dentro de qualquer pasta 'templates' no projeto
      '../../**/templates/**/*.html',
      
      // Garante especificamente a pasta do seu tema
      '../../theme/**/*.html',
      
      // Se você usar classes em arquivos Python (forms.py, views.py), descomente abaixo:
      // '../../**/forms.py',
  ],
  theme: {
    extend: {
      colors: {
        // Base do vidro
        'glass-base': 'rgba(255, 255, 255, 0.70)', 
        'glass-border': 'rgba(0, 0, 0, 0.06)', 
        'glass-shadow': 'rgba(0, 0, 0, 0.04)',
      },
      backdropBlur: {
        'thin': '12px',     
        'regular': '30px',   
      },
      boxShadow: {
        'glass': '0 4px 20px -2px rgba(0, 0, 0, 0.05)',
      }
    },
  },
  plugins: [],
}