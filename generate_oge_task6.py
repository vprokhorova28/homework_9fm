from IPython.core.display import HTML, display
from random import choice, randint

def generate_oge_task6():
    t1 = 'Ниже приведена программа, записанная на пяти языках программирования.\n'
    s = choice(['&gt', '&lt'])
    n = randint(3, 15)
    a = '{'
    html = '''<center><p></p><p></p><table border="" width="55%"><tbody><tr><th width="50%"><b>Бейсик</b></th><th width="50%"><b>Python</b></th></tr><tr><td><div class="source_code lang_python"><pre class="sh_basic sh_sourceCode"><span class="sh_basic_strange_words">DIM</span> s<span class="sh_symbol">,</span> t <span class="sh_basic_strange_words">AS</span> <span class="sh_type">INTEGER</span>
 <span class="sh_basic_strange_words">INPUT</span> s
 <span class="sh_basic_strange_words">INPUT</span> t
 <span class="sh_keyword">IF</span> s ''' + f'<span class="sh_symbol">{s};</span> <span class="sh_number">{n}</span> OR t <span class="sh_symbol">{s};</span> <span class="sh_number">{n}</span>' + '''<span class="sh_keyword"> THEN</span>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="sh_basic_strange_words">PRINT</span> ‘ДА’
 <span class="sh_basic_strange_words">ELSE</span>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="sh_basic_strange_words">PRINT</span> ‘НЕТ’
 <span class="sh_keyword">ENDIF</span></pre></div></td><td><div class="source_code lang_python" style="font-family:monospace"><p>s = int(input())</p><p>t = int(input())</p><p>''' + f'if s {s}; {n} or t {s}; {n}:</p><p>&nbsp;&nbsp;&nbsp;&nbsp;print("ДА")</p><p>else:</p><p>&nbsp;&nbsp;&nbsp;&nbsp;print("НЕТ")</p><p> </p></div><p> </p></td></tr><tr><th><b>Паскаль</b></th><th><b>Алгоритмический язык</b></th></tr><tr><td><div class="source_code lang_pascal"><pre class="sh_pascal sh_sourceCode"><span class="sh_keyword">var</span> s<span class="sh_symbol">,</span> t<span class="sh_symbol">:</span>' + '''<span class="sh_type">integer</span><span class="sh_symbol">;</span>
<span class="sh_keyword">begin</span>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="sh_keyword">readln</span><span class="sh_symbol">(</span>s<span class="sh_symbol">);</span>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="sh_keyword">readln</span><span class="sh_symbol">(</span>t<span class="sh_symbol">);</span>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="sh_keyword">if''' + f'</span> <span class="sh_symbol">(</span>s <span class="sh_symbol">{s};</span> <span class="sh_number">{n}</span><span class="sh_symbol">)</span> <span class="sh_keyword">or</span> <span class="sh_symbol">(</span>t <span class="sh_symbol">{s};</span> <span class="sh_number">{n}</span><span class="sh_symbol">)' + '''</span>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sh_keyword">then</span> <span class="sh_keyword">writeln</span><span class="sh_symbol">(</span><span class="sh_string_pasc">'ДА'</span><span class="sh_symbol">)</span>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sh_keyword">else</span> <span class="sh_keyword">writeln</span><span class="sh_symbol">(</span><span class="sh_string_pasc">'НЕТ'</span><span class="sh_symbol">)</span>
<span class="sh_keyword">end</span><span class="sh_symbol">.</span></pre></div></td><td><div class="source_code lang_pascal"><pre class="sh_alg sh_sourceCode"><span class="sh_alg_keyword">алг</span>
<span class="sh_alg_keyword">нач</span>
<span class="sh_alg_keyword">цел</span> s<span class="sh_symbol">,</span> t
<span class="sh_alg_keyword">ввод</span> s
<span class="sh_alg_keyword">ввод</span> t
<span class="sh_alg_keyword">если</span> s''' + f' <span class="sh_symbol">{s};</span> <span class="sh_number">{n}</span> или t <span class="sh_symbol">{s};</span> <span class="sh_number">{n}' + '''</span>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="sh_alg_keyword">то</span> <span class="sh_alg_keyword">вывод</span> "ДА"
&nbsp;&nbsp;&nbsp;&nbsp;<span class="sh_alg_keyword">иначе</span> <span class="sh_alg_keyword">вывод</span> "НЕТ"
<span class="sh_alg_keyword">все</span>
<span class="sh_alg_keyword">кон</span></pre></div></td></tr><tr><th colspan="2"><b>С++</b></th></tr><tr><td colspan="2"><div class="source_code lang_pascal"><pre class="sh_c sh_sourceCode"><span class="sh_preproc">#include</span> <span class="sh_string">&lt;iostream&gt;</span>
using <span class="sh_usertype">namespace</span><span class="sh_normal"> </span>std<span class="sh_symbol">;</span>
<span class="sh_type">int</span> <span class="sh_function">main</span><span class="sh_symbol">()</span> <span class="sh_cbracket">{</span>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="sh_type">int</span> s<span class="sh_symbol">,</span> t<span class="sh_symbol">;</span>
&nbsp;&nbsp;&nbsp;&nbsp;cin <span class="sh_symbol">&gt;&gt;</span> s<span class="sh_symbol">;</span>
&nbsp;&nbsp;&nbsp;&nbsp;cin <span class="sh_symbol">&gt;&gt;</span> t<span class="sh_symbol">;</span>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="sh_keyword">if</span> <span class="sh_symbol">(</span>s ''' + f'<span class="sh_symbol">{s};</span> <span class="sh_number">{n}</span> <span class="sh_symbol">||</span> t <span class="sh_symbol">{s};</span> <span class="sh_number">{n}</span><span class="sh_symbol">)' + '''</span>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cout <span class="sh_symbol">&lt;&lt;</span> <span class="sh_string">"ДА"</span><span class="sh_symbol">;</span>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="sh_keyword">else</span>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cout <span class="sh_symbol">&lt;&lt;</span> <span class="sh_string">"НЕТ"</span><span class="sh_symbol">;</span>
<span class="sh_keyword">return</span> <span class="sh_number">0</span><span class="sh_symbol">;</span>
<span class="sh_cbracket">}</span></pre></div></td></tr></tbody></table><p>&nbsp;</p></center>'''
    num = []
    for i in range(9):
        num.append((randint(-15, 15), randint(-15, 15)))
    answer = 0
    for i in range(9):
        s, t = num[i]
        if s == '&gt':
            if s > n or t > n:
                answer += 1
        else:
            if s < n or t < n:
                answer += 1
    num = [str(i) for i in num]
    j = '; '.join(num)
    t2 = f'Было проведено 9 запусков программы, при которых в качестве значений переменных s и t вводились следующие пары чисел:\n\n'\
         f'\t\t{j}.\n\n'\
         f'\tСколько было запусков, при которых программа напечатала «ДА»?'
    print(t1)
    display(HTML(html))
    print(t2)
    return(answer)
    
generate_oge_task6()
