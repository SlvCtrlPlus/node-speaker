{
  'targets': [
    {
      'target_name': 'speaker',
      'sources': [
        'src/binding.c',
      ],
      'dependencies': [
        'deps/mpg123/mpg123.gyp:output'
      ],
    }
  ]
}
