from django.http.response import HttpResponseForbidden


# FILTRA IP MIDDLEWARE
# ----------------------------------------

class FiltraIPMiddleware:

    def __init__(self, get_response=None):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        # Lista de IPs autorizados
        ips_autorizados = ['127.0.0.1']

        # IP do usuário
        ip_usuario = request.META.get('REMOTE_ADDR')  

        # Verifica se é um IP autorizado
        if ip_usuario not in ips_autorizados:
            # Se não for
            return HttpResponseForbidden("IP não autorizado")

        # Se for um IP autorizado, não fazemos nada
        return None
