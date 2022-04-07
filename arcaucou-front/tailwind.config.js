module.exports = {
  darkMode: 'class',
  theme: {
    colors: {
      'd-background': '#001E26',
      'd-60': '#012A35',
      'd-30': '#003543',
      'd-10': '#00DC82',
      'd-text': '#FFFF',
      'l-background': '#FFFF',
      'l-60': '#42B883',
      'l-30': '#42B883',
      'l-10': '#00DC82',
      'l-text': '#000',
      red: '#ba0000',
      gray: '#808080',
    },
  },
  plugins: [require('tailwind-scrollbar')],
  variants: {
    scrollbar: ['dark', 'rounded'],
  },
}
