# shopt -s extglob for extended glob functionality

Put 'shopt -s extglob' in your .bashrc or .bash_profile to enable this option.

If the extglob shell option is enabled using the shopt builtin, several
extended pattern matching operators are recognized.  In  the  following
description, a pattern-list is a list of one or more patterns separated
by a |.  Composite patterns may be formed using  one  or  more  of  the
following sub-patterns:

      ?(pattern-list)
             Matches zero or one occurrence of the given patterns
      *(pattern-list)
             Matches zero or more occurrences of the given patterns
      +(pattern-list)
             Matches one or more occurrences of the given patterns
      @(pattern-list)
             Matches one of the given patterns
      !(pattern-list)
             Matches anything except one of the given patterns

Good examples on how to use it:<br>
[Linux Journal - bash extended globbing](https://www.linuxjournal.com/content/bash-extended-globbing)<br>
[Greg's Wiki - extglob](http://mywiki.wooledge.org/glob#extglob)
