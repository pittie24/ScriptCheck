from django.shortcuts import render
from django.http import HttpResponse
from rules.regex_rules import test_regex_rules


def test_regex_view(request):
    sample_text = "Halo,, nama saya budi. saya tinggal di bandung!! saya suka kopi.. "
    results = test_regex_rules(sample_text)
    
    output = "Hasil Deteksi:\n\n"
    for r in results:
        output += f"- {r['rule']}: {r['matches']}\n"
    return HttpResponse(f"<pre>{output}</pre>")
