// tailwind.config.js

module.exports = {
  content: [
    // ... seus caminhos
  ],
  theme: {
    extend: {
      colors: {
        // Base do vidro (Branco quase opaco para fundos claros)
        'glass-base': 'rgba(255, 255, 255, 0.70)', 
        
        // IMPORTANTE: Bordas para tema claro (Preto com baixa opacidade)
        // Isso cria a definição nítida necessária em fundos brancos
        'glass-border': 'rgba(0, 0, 0, 0.06)', 
        
        // Sombra ambiente para dar profundidade sutil
        'glass-shadow': 'rgba(0, 0, 0, 0.04)',
      },
      
      backdropBlur: {
        'thin': '12px',     
        'regular': '30px',   
      },
      
      boxShadow: {
        // Sombra suave e difusa para levantar o vidro do fundo branco
        'glass': '0 4px 20px -2px rgba(0, 0, 0, 0.05)',
      }
    },
  },
  plugins: [],
};