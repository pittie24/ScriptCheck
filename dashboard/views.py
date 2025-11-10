from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def dashboard_view(request):
    """
    Menampilkan dashboard utama ScriptCheck untuk pengguna yang sudah login.
    """
    context = {
        'total_docs': 8,
        'errors_found': 14,
        'latest_upload': "report_final_2025.pdf",
    }
    return render(request, 'dashboard/dashboard.html', context)
