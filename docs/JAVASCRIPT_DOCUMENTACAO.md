# ⚡ JavaScript no Quasar Cronos - Documentação Completa

![JavaScript](https://img.shields.io/badge/JavaScript-ES6-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![Bootstrap JS](https://img.shields.io/badge/Bootstrap_JS-5.3-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)
![Vanilla JS](https://img.shields.io/badge/Vanilla_JS-No_Frameworks-61DAFB?style=for-the-badge)

## 📋 **Visão Geral**

O **Quasar Cronos** utiliza **JavaScript ES6** de forma estratégica e minimalista, focando em funcionalidades essenciais sem dependências externas além do Bootstrap. Esta documentação detalha todo o código JavaScript presente no projeto, sua localização, propósito e funcionamento.

---

## 🎯 **Filosofia JavaScript do Projeto**

### ✅ **Abordagem Adotada**
- **Vanilla JavaScript** (sem frameworks pesados)
- **Progressive Enhancement** (funciona sem JS)
- **Bootstrap JavaScript** para componentes básicos
- **Código inline** em templates (simplicidade)
- **ES6 features** (fetch, arrow functions, const/let)

### ❌ **O que NÃO é usado**
- React, Vue, Angular (frameworks SPA)
- jQuery (desnecessário com ES6)
- TypeScript (mantém simplicidade)
- Bundle tools (Webpack, Vite)
- NPM packages locais

---

## 📍 **Localização de Todo JavaScript**

### 🌐 **1. Bootstrap JavaScript (CDN)**
**📁 Arquivo:** `templates/base.html`  
**📍 Linha:** 248
```html
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
```

### 🔔 **2. Sistema de Notificações (Inline)**
**📁 Arquivo:** `templates/base.html`  
**📍 Linhas:** 252-276
```javascript
function atualizarNotificacoes() {
    fetch('{% url "demandas:notificacoes_json" %}')
        .then(response => response.json())
        .then(data => {
            const badge = document.getElementById('badge-notificacoes');
            const count = document.getElementById('count-notificacoes');
            
            if (data.total > 0) {
                count.textContent = data.total;
                badge.style.display = 'inline-block';
                badge.title = `${data.atrasadas} atrasadas, ${data.prazo_proximo} com prazo próximo`;
            } else {
                badge.style.display = 'none';
            }
        })
        .catch(error => console.log('Erro ao carregar notificações:', error));
}

// Atualizar ao carregar a página
document.addEventListener('DOMContentLoaded', atualizarNotificacoes);

// Atualizar a cada 2 minutos
setInterval(atualizarNotificacoes, 120000);
```

### 🗑️ **3. Confirmação de Exclusão (Template)**
**📁 Arquivo:** `demandas/templates/demandas/demanda_confirm_delete.html`  
**📍 Linhas:** 295-368
```javascript
document.addEventListener('DOMContentLoaded', function() {
    const codigoOriginal = '{{ object.codigo }}';
    const inputConfirmacao = document.getElementById('confirmacao');
    const btnConfirmar = document.getElementById('btnConfirmarExclusao');
    
    // Validação em tempo real
    inputConfirmacao.addEventListener('input', function() {
        const valorDigitado = this.value.trim();
        
        if (valorDigitado === codigoOriginal) {
            btnConfirmar.disabled = false;
            btnConfirmar.classList.add('btn-danger');
            this.classList.add('is-valid');
        } else {
            btnConfirmar.disabled = true;
            this.classList.add('is-invalid');
        }
    });
    
    // Prevenir envio acidental
    btnConfirmar.addEventListener('click', function() {
        return confirm('Tem certeza que deseja excluir esta demanda?');
    });
});
```

### 📝 **4. Auto-resize de Textarea (Template)**
**📁 Arquivo:** `demandas/templates/demandas/demanda_detail.html`  
**📍 Linhas:** 427-442
```javascript
// Auto-resize textarea
document.querySelectorAll('textarea').forEach(function(textarea) {
    textarea.addEventListener('input', function() {
        this.style.height = 'auto';
        this.style.height = this.scrollHeight + 'px';
    });
});

// AJAX para comentários (preparado para futuro)
document.getElementById('comentarioForm').addEventListener('submit', function(e) {
    // Para implementação futura de comentários via AJAX
});
```

### 🧪 **5. Teste de Background (Desenvolvimento)**
**📁 Arquivo:** `teste_background.html`  
**📍 Linhas:** 61-117
```javascript
function runTests() {
    const statusDiv = document.getElementById('status');
    const detailsDiv = document.getElementById('details');
    
    const testUrls = [
        '/static/demandas/images/background-login.jpg',
        '../static/demandas/images/background-login.jpg', 
        './demandas/static/demandas/images/background-login.jpg',
        'http://127.0.0.1:8000/static/demandas/images/background-login.jpg'
    ];
    
    testUrls.forEach((url, index) => {
        const img = new Image();
        img.onload = function() {
            results.push(`✅ URL ${index + 1}: ${url} - SUCESSO`);
        };
        img.onerror = function() {
            results.push(`❌ URL ${index + 1}: ${url} - FALHOU`);
        };
        img.src = url;
    });
}
```

### 🔐 **6. Login - Funcionalidade Mínima**
**📁 Arquivo:** `templates/registration/login.html`  
**📍 Linha:** 179
```html
<a href="#" onclick="alert('Funcionalidade em desenvolvimento')">
```

---

## 🎯 **Funcionalidades JavaScript Detalhadas**

### 🔔 **1. Sistema de Notificações (Tempo Real)**

#### 🎯 **Propósito**
Atualizar automaticamente o badge de notificações na navbar sem recarregar a página.

#### 🔧 **Como Funciona**
1. **Fetch API** faz requisição para `demandas:notificacoes_json`
2. **JSON Response** retorna dados das notificações
3. **DOM Manipulation** atualiza badge e contador
4. **Auto-refresh** a cada 2 minutos (120.000ms)

#### 📡 **Endpoint Django**
```python
# demandas/urls.py
path('notificacoes/', views.notificacoes_json, name='notificacoes_json'),

# demandas/views.py  
def notificacoes_json(request):
    return JsonResponse({
        'total': 5,
        'atrasadas': 2, 
        'prazo_proximo': 3
    })
```

#### 🎨 **UI Modificada**
- **Badge visibility:** `display: none/inline-block`
- **Counter text:** `textContent = data.total`
- **Tooltip:** `title = "${data.atrasadas} atrasadas..."`

### 🗑️ **2. Confirmação de Exclusão (Segurança)**

#### 🎯 **Propósito**
Prevenir exclusões acidentais exigindo digitação do código da demanda.

#### 🔧 **Como Funciona**
1. **Input validation** em tempo real
2. **Button state** habilitado apenas com código correto
3. **CSS classes** para feedback visual (`is-valid`, `is-invalid`)
4. **Confirm dialog** como segunda camada de segurança

#### 🎨 **Estados do Botão**
```javascript
// Estado inicial: desabilitado
btnConfirmar.disabled = true;
btnConfirmar.classList.add('btn-outline-danger');

// Estado válido: habilitado 
btnConfirmar.disabled = false;
btnConfirmar.classList.add('btn-danger');
```

#### 🚫 **Proteções Implementadas**
- **Real-time validation:** `addEventListener('input')`
- **Paste prevention:** Bloqueia Ctrl+V
- **Enter key handling:** `addEventListener('keypress')`
- **Focus/Blur events:** Visual feedback
- **Double confirmation:** `confirm()` dialog

### 📝 **3. Auto-resize Textarea (UX)**

#### 🎯 **Propósito**
Melhorar experiência de usuário expandindo textarea automaticamente.

#### 🔧 **Como Funciona**
1. **Event listener** no evento `input`
2. **Height reset:** `this.style.height = 'auto'`
3. **Dynamic sizing:** `this.style.height = this.scrollHeight + 'px'`
4. **Applied to all:** `querySelectorAll('textarea')`

#### 💡 **Vantagens UX**
- ✅ Sem scroll interno no textarea
- ✅ Visualização completa do conteúdo
- ✅ Adaptação automática ao texto
- ✅ Funciona em qualquer textarea

### 🧪 **4. Sistema de Testes (Desenvolvimento)**

#### 🎯 **Propósito**
Validar carregamento de imagens de background durante desenvolvimento.

#### 🔧 **Como Funciona**
1. **Image objects** para testar URLs
2. **onload/onerror** handlers para resultado
3. **Promise-like** completion tracking
4. **Visual feedback** com status colorido

#### 🎨 **Feedback Visual**
```javascript
// Status classes
.status.info { background: #0dcaf0; }
.status.success { background: #198754; }
.status.error { background: #dc3545; }
```

---

## 🎮 **Bootstrap JavaScript Integrado**

### 📱 **Componentes Ativos**

#### 1. **Navbar Collapse (Mobile)**
```html
<button data-bs-toggle="collapse" data-bs-target="#navbarNav">
```
**Funcionalidade:** Menu hambúrguer responsivo

#### 2. **Dropdown Menu (Usuário)**
```html
<a data-bs-toggle="dropdown">
```
**Funcionalidade:** Menu dropdown do usuário logado

#### 3. **Tabs (Detalhes de Demanda)**
```html
<button data-bs-toggle="tab" data-bs-target="#comentarios">
```
**Funcionalidade:** Navegação entre comentários/histórico/anexos

#### 4. **Alerts Dismissible**
```html
<button data-bs-dismiss="alert">
```
**Funcionalidade:** Fechar alertas manualmente

### ⚡ **Auto-inicialização Bootstrap**
O Bootstrap 5.3 inicializa automaticamente todos os componentes com `data-bs-*` attributes.

---

## 📊 **Padrões de Código Utilizados**

### 🎯 **1. Event Listeners Modernos**
```javascript
// ✅ Moderno (ES6)
document.addEventListener('DOMContentLoaded', function() {
    // código aqui
});

// ❌ Antigo (evitado)
window.onload = function() { }
```

### 🎯 **2. Fetch API (não XMLHttpRequest)**
```javascript
// ✅ Moderno (ES6)
fetch('{% url "demandas:notificacoes_json" %}')
    .then(response => response.json())
    .then(data => {
        // processar dados
    })
    .catch(error => console.log(error));

// ❌ Antigo (evitado)
var xhr = new XMLHttpRequest();
```

### 🎯 **3. Query Selectors (não getElementById)**
```javascript
// ✅ Flexível
const badge = document.getElementById('badge-notificacoes');
const textareas = document.querySelectorAll('textarea');

// ✅ Quando apropriado
document.querySelector('.login-form');
```

### 🎯 **4. Arrow Functions**
```javascript
// ✅ Moderno (ES6)
textareas.forEach(textarea => {
    textarea.addEventListener('input', () => {
        // código aqui
    });
});
```

### 🎯 **5. Template Literals (Django Integration)**
```javascript
// ✅ Integração Django + ES6
badge.title = `${data.atrasadas} atrasadas, ${data.prazo_proximo} com prazo próximo`;
```

---

## 🔄 **Integração com Django**

### 🌐 **1. URLs Django em JavaScript**
```javascript
// Template tag para URLs seguras
fetch('{% url "demandas:notificacoes_json" %}')

// Variáveis Django no JS
const codigoOriginal = '{{ object.codigo }}';
```

### 📡 **2. CSRF Protection**
```html
<!-- Token CSRF automático em forms -->
{% csrf_token %}

<!-- Para AJAX futuro -->
const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
```

### 🎯 **3. Context Variables**
```javascript
// Django context no JavaScript
const demandaId = {{ object.id }};
const userId = {{ user.id }};
const isStaff = {{ user.is_staff|yesno:"true,false" }};
```

---

## 📱 **Responsividade JavaScript**

### 🔧 **Breakpoint-aware Code**
```javascript
// Detectar largura da tela
function isMobile() {
    return window.innerWidth < 768;
}

// Comportamento adaptativo
if (isMobile()) {
    // código específico mobile
} else {
    // código desktop
}
```

### 📏 **Media Query Listeners**
```javascript
// Escutar mudanças de tamanho
window.addEventListener('resize', function() {
    // ajustar interface
});

// CSS Media Query em JS
const mediaQuery = window.matchMedia('(max-width: 768px)');
mediaQuery.addListener(function(e) {
    if (e.matches) {
        // mobile
    }
});
```

---

## 🛡️ **Segurança JavaScript**

### 🔒 **Práticas de Segurança Implementadas**

#### 1. **XSS Prevention**
```javascript
// ✅ Seguro - textContent (não innerHTML)
count.textContent = data.total;

// ❌ Perigoso - innerHTML com dados externos
// element.innerHTML = userInput;
```

#### 2. **Input Validation**
```javascript
// ✅ Validação client-side
const valorDigitado = this.value.trim();
if (valorDigitado === codigoOriginal) {
    // ação segura
}
```

#### 3. **Error Handling**
```javascript
// ✅ Tratamento de erros
.catch(error => console.log('Erro ao carregar notificações:', error));
```

#### 4. **Safe Event Handlers**
```javascript
// ✅ Confirma ações destrutivas
btnConfirmar.addEventListener('click', function() {
    return confirm('Tem certeza que deseja excluir esta demanda?');
});
```

---

## ⚡ **Performance JavaScript**

### 🚀 **Otimizações Implementadas**

#### 1. **Event Delegation**
```javascript
// ✅ Eficiente para múltiplos elementos
document.querySelectorAll('textarea').forEach(function(textarea) {
    textarea.addEventListener('input', resizeFunction);
});
```

#### 2. **Debouncing (implícito)**
```javascript
// Notificações: apenas a cada 2 minutos
setInterval(atualizarNotificacoes, 120000);
```

#### 3. **DOM Ready Optimization**
```javascript
// ✅ Aguarda DOM completo
document.addEventListener('DOMContentLoaded', function() {
    // inicialização segura
});
```

#### 4. **Minimal DOM Queries**
```javascript
// ✅ Cache de elementos
const badge = document.getElementById('badge-notificacoes');
const count = document.getElementById('count-notificacoes');
```

---

## 🧪 **Debugging JavaScript**

### 🔍 **Ferramentas de Debug**

#### 1. **Console Logging**
```javascript
console.log('Erro ao carregar notificações:', error);
console.log('Dados recebidos:', data);
```

#### 2. **DevTools Integration**
```javascript
// Verificar se função existe
typeof atualizarNotificacoes === 'function'

// Testar manualmente
atualizarNotificacoes();
```

#### 3. **Error Boundaries**
```javascript
try {
    // código que pode falhar
    fetch(url).then(response => response.json())
} catch (error) {
    console.error('Erro capturado:', error);
}
```

### 🐛 **Troubleshooting Common Issues**

#### 1. **Fetch não funciona**
```javascript
// Verificar URL
console.log('URL:', '{% url "demandas:notificacoes_json" %}');

// Verificar response
.then(response => {
    console.log('Status:', response.status);
    return response.json();
})
```

#### 2. **Elements não encontrados**
```javascript
// Verificar se elemento existe
const element = document.getElementById('badge-notificacoes');
if (element) {
    // código seguro
} else {
    console.error('Elemento não encontrado');
}
```

#### 3. **Event listeners não funcionam**
```javascript
// Verificar timing
document.addEventListener('DOMContentLoaded', function() {
    // garantir que DOM está pronto
    const element = document.getElementById('target');
    if (element) {
        element.addEventListener('click', handler);
    }
});
```

---

## 📚 **Estrutura de Arquivos JavaScript**

### 📁 **Organização Atual**
```
📦 gestao_demandas_projeto/
├── 📄 templates/base.html                    # Bootstrap JS + Notificações
├── 📄 templates/registration/login.html      # JavaScript mínimo
├── 📄 demandas/templates/demandas/
│   ├── demanda_confirm_delete.html          # Validação de exclusão
│   ├── demanda_detail.html                  # Auto-resize textarea
│   └── ...
├── 📄 teste_background.html                 # Testes de desenvolvimento
└── 🚫 static/js/                            # (não existe - inline approach)
```

### 🎯 **Justificativa da Estrutura**
- **Inline JavaScript:** Simplicidade e acesso direto ao contexto Django
- **Sem arquivos .js separados:** Evita complexidade de build tools
- **Template-specific:** Cada funcionalidade fica próxima ao HTML
- **CDN para Bootstrap:** Sem necessidade de bundle local

---

## 🔄 **Futuras Expansões JavaScript**

### 🚀 **Funcionalidades Planejadas**

#### 1. **AJAX Comments**
```javascript
// Em demanda_detail.html - preparado para implementação
document.getElementById('comentarioForm').addEventListener('submit', function(e) {
    e.preventDefault();
    
    const formData = new FormData(this);
    fetch('{% url "demandas:comentario_ajax" %}', {
        method: 'POST',
        body: formData,
        headers: {
            'X-CSRFToken': csrftoken
        }
    })
    .then(response => response.json())
    .then(data => {
        // atualizar lista de comentários
    });
});
```

#### 2. **Real-time Status Updates**
```javascript
// WebSocket ou Server-Sent Events
const eventSource = new EventSource('{% url "demandas:status_stream" %}');
eventSource.onmessage = function(event) {
    const data = JSON.parse(event.data);
    updateDemandaStatus(data);
};
```

#### 3. **Advanced Filters**
```javascript
// Filtros dinâmicos na lista
function filterDemandas() {
    const filters = {
        status: document.getElementById('filter-status').value,
        categoria: document.getElementById('filter-categoria').value
    };
    
    fetch('{% url "demandas:lista_filtered" %}', {
        method: 'POST',
        body: JSON.stringify(filters)
    })
    .then(response => response.json())
    .then(data => updateTable(data));
}
```

### 📋 **Roadmap Técnico**
- ✅ **Fase 1:** Funcionalidades básicas (completa)
- 🔄 **Fase 2:** AJAX para comentários
- 🔜 **Fase 3:** Real-time updates
- 🔜 **Fase 4:** Advanced filtering
- 🔜 **Fase 5:** PWA features

---

## ✅ **Checklist JavaScript**

### 🎯 **JavaScript no Projeto**
- ✅ Bootstrap 5.3 JS via CDN
- ✅ Sistema de notificações em tempo real
- ✅ Validação de exclusão de demandas
- ✅ Auto-resize de textareas
- ✅ Teste de carregamento de imagens
- ✅ Event listeners modernos (ES6)
- ✅ Fetch API para requisições
- ✅ Error handling implementado
- ✅ Integração segura com Django
- ✅ Práticas de segurança (XSS prevention)

### 🚀 **Próximos Passos**
- 🔄 Implementar AJAX para comentários
- 📱 Adicionar PWA service worker
- 🎯 Real-time notifications com WebSocket
- 📊 Charts.js para dashboards
- 🔍 Advanced search/filtering

---

## 📖 **Recursos e Documentação**

### 🔗 **Links Úteis**
- **MDN JavaScript:** https://developer.mozilla.org/en-US/docs/Web/JavaScript
- **Fetch API:** https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API
- **Bootstrap JS:** https://getbootstrap.com/docs/5.3/getting-started/javascript/
- **Django + JS:** https://docs.djangoproject.com/en/4.2/ref/csrf/

### 📚 **Documentação Específica**
- **ES6 Features:** Arrow functions, fetch, const/let, template literals
- **DOM API:** addEventListener, querySelector, classList
- **Bootstrap Components:** Dropdowns, collapse, tabs, alerts

---

<div align="center">

**⚡ JavaScript ES6 - Interatividade do Quasar Cronos**

![Vanilla JS](https://img.shields.io/badge/Vanilla-JS-F7DF1E?style=flat-square)
![Modern](https://img.shields.io/badge/ES6-Ready-success?style=flat-square)
![Bootstrap](https://img.shields.io/badge/Bootstrap-Integrated-7952B3?style=flat-square)

</div>