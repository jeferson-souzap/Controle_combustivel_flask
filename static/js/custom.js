// Custom JavaScript para Sistema de Cadastros

document.addEventListener('DOMContentLoaded', function() {
    
    // Inicialização
    initializeFormValidation();
    initializeInputMasks();
    initializeTooltips();
    initializeAnimations();
    initializeFormSubmission();
    
    console.log('Sistema de Cadastros inicializado com sucesso!');
});

// Validação de formulários
function initializeFormValidation() {
    const forms = document.querySelectorAll('.needs-validation');
    
    Array.from(forms).forEach(form => {
        form.addEventListener('submit', function(event) {
            if (!form.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
                
                // Foca no primeiro campo inválido
                const firstInvalidField = form.querySelector(':invalid');
                if (firstInvalidField) {
                    firstInvalidField.focus();
                    firstInvalidField.scrollIntoView({ behavior: 'smooth', block: 'center' });
                }
            }
            
            form.classList.add('was-validated');
        });
        
        // Validação em tempo real
        const inputs = form.querySelectorAll('input, select, textarea');
        inputs.forEach(input => {
            input.addEventListener('blur', function() {
                if (this.checkValidity()) {
                    this.classList.remove('is-invalid');
                    this.classList.add('is-valid');
                } else {
                    this.classList.remove('is-valid');
                    this.classList.add('is-invalid');
                }
            });
        });
    });
}

// Máscaras de entrada
function initializeInputMasks() {
    // Máscara para CPF
    const cpfInputs = document.querySelectorAll('input[name="cpf"]');
    cpfInputs.forEach(input => {
        input.addEventListener('input', function(e) {
            let value = e.target.value.replace(/\D/g, '');
            value = value.replace(/(\d{3})(\d)/, '$1.$2');
            value = value.replace(/(\d{3})(\d)/, '$1.$2');
            value = value.replace(/(\d{3})(\d{1,2})$/, '$1-$2');
            e.target.value = value;
        });
        
        // Validação de CPF
        input.addEventListener('blur', function(e) {
            const cpf = e.target.value.replace(/\D/g, '');
            if (cpf.length === 11 && !isValidCPF(cpf)) {
                e.target.setCustomValidity('CPF inválido');
                e.target.classList.add('is-invalid');
            } else {
                e.target.setCustomValidity('');
                e.target.classList.remove('is-invalid');
            }
        });
    });
    
    // Máscara para telefone
    const phoneInputs = document.querySelectorAll('input[name="telefone"]');
    phoneInputs.forEach(input => {
        input.addEventListener('input', function(e) {
            let value = e.target.value.replace(/\D/g, '');
            if (value.length <= 10) {
                value = value.replace(/(\d{2})(\d)/, '($1) $2');
                value = value.replace(/(\d{4})(\d)/, '$1-$2');
            } else {
                value = value.replace(/(\d{2})(\d)/, '($1) $2');
                value = value.replace(/(\d{5})(\d)/, '$1-$2');
            }
            e.target.value = value;
        });
    });
}

// Validação de CPF
function isValidCPF(cpf) {
    if (cpf.length !== 11 || /^(\d)\1{10}$/.test(cpf)) {
        return false;
    }
    
    let sum = 0;
    for (let i = 0; i < 9; i++) {
        sum += parseInt(cpf.charAt(i)) * (10 - i);
    }
    let remainder = 11 - (sum % 11);
    if (remainder === 10 || remainder === 11) remainder = 0;
    if (remainder !== parseInt(cpf.charAt(9))) return false;
    
    sum = 0;
    for (let i = 0; i < 10; i++) {
        sum += parseInt(cpf.charAt(i)) * (11 - i);
    }
    remainder = 11 - (sum % 11);
    if (remainder === 10 || remainder === 11) remainder = 0;
    if (remainder !== parseInt(cpf.charAt(10))) return false;
    
    return true;
}

// Inicializar tooltips
function initializeTooltips() {
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function(tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });
}

// Animações e efeitos visuais
function initializeAnimations() {
    // Smooth scroll para links de navegação
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
    
    // Animação de entrada para cards
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, observerOptions);
    
    document.querySelectorAll('.card').forEach(card => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(20px)';
        card.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        observer.observe(card);
    });
}

// Melhorias na submissão de formulários
function initializeFormSubmission() {
    const forms = document.querySelectorAll('form');
    
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            const submitBtn = form.querySelector('button[type="submit"]');
            if (submitBtn && form.checkValidity()) {
                // Adiciona estado de loading
                submitBtn.classList.add('loading');
                submitBtn.disabled = true;
                
                // Remove o loading após um tempo (caso não haja redirecionamento)
                setTimeout(() => {
                    submitBtn.classList.remove('loading');
                    submitBtn.disabled = false;
                }, 3000);
            }
        });
    });
}

// Confirmação para ações de remoção
document.addEventListener('click', function(e) {
    if (e.target.closest('button[onclick*="confirm"]')) {
        const button = e.target.closest('button');
        const confirmMessage = button.getAttribute('onclick').match(/confirm\('([^']+)'\)/);
        if (confirmMessage) {
            e.preventDefault();
            showConfirmModal(confirmMessage[1], function() {
                button.closest('form').submit();
            });
        }
    }
});

// Modal de confirmação personalizado
function showConfirmModal(message, onConfirm) {
    // Remove modal existente se houver
    const existingModal = document.getElementById('confirmModal');
    if (existingModal) {
        existingModal.remove();
    }
    
    // Cria o modal
    const modalHTML = `
        <div class="modal fade" id="confirmModal" tabindex="-1" aria-labelledby="confirmModalLabel" aria-hidden="true">
            <div class="modal-dialog modal-dialog-centered">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title" id="confirmModalLabel">
                            <i class="bi bi-exclamation-triangle text-warning me-2"></i>
                            Confirmação
                        </h5>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        <p class="mb-0">${message}</p>
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">
                            <i class="bi bi-x-circle me-1"></i>Cancelar
                        </button>
                        <button type="button" class="btn btn-danger" id="confirmBtn">
                            <i class="bi bi-check-circle me-1"></i>Confirmar
                        </button>
                    </div>
                </div>
            </div>
        </div>
    `;
    
    document.body.insertAdjacentHTML('beforeend', modalHTML);
    
    const modal = new bootstrap.Modal(document.getElementById('confirmModal'));
    const confirmBtn = document.getElementById('confirmBtn');
    
    confirmBtn.addEventListener('click', function() {
        modal.hide();
        onConfirm();
    });
    
    modal.show();
    
    // Remove o modal do DOM quando fechado
    document.getElementById('confirmModal').addEventListener('hidden.bs.modal', function() {
        this.remove();
    });
}

// Notificações toast
function showToast(message, type = 'success') {
    // Remove toast existente se houver
    const existingToast = document.getElementById('customToast');
    if (existingToast) {
        existingToast.remove();
    }
    
    const toastHTML = `
        <div class="toast-container position-fixed top-0 end-0 p-3">
            <div id="customToast" class="toast" role="alert" aria-live="assertive" aria-atomic="true">
                <div class="toast-header">
                    <i class="bi bi-${type === 'success' ? 'check-circle text-success' : 'exclamation-triangle text-danger'} me-2"></i>
                    <strong class="me-auto">Sistema de Cadastros</strong>
                    <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>
                </div>
                <div class="toast-body">
                    ${message}
                </div>
            </div>
        </div>
    `;
    
    document.body.insertAdjacentHTML('beforeend', toastHTML);
    
    const toast = new bootstrap.Toast(document.getElementById('customToast'));
    toast.show();
    
    // Remove o toast do DOM quando fechado
    document.getElementById('customToast').addEventListener('hidden.bs.toast', function() {
        this.closest('.toast-container').remove();
    });
}

// Função para limpar formulários
function clearForm(formId) {
    const form = document.getElementById(formId);
    if (form) {
        form.reset();
        form.classList.remove('was-validated');
        
        // Remove classes de validação dos campos
        const inputs = form.querySelectorAll('input, select, textarea');
        inputs.forEach(input => {
            input.classList.remove('is-valid', 'is-invalid');
        });
        
        showToast('Formulário limpo com sucesso!');
    }
}

// Função para buscar dados via AJAX (exemplo)
async function fetchData(url) {
    try {
        const response = await fetch(url);
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return await response.json();
    } catch (error) {
        console.error('Erro ao buscar dados:', error);
        showToast('Erro ao carregar dados', 'error');
        return null;
    }
}

// Função para atualizar tabelas dinamicamente
async function refreshTable(tableType) {
    const loadingSpinner = `
        <tr>
            <td colspan="100%" class="text-center">
                <div class="spinner-border spinner-border-sm text-primary" role="status">
                    <span class="visually-hidden">Carregando...</span>
                </div>
                <span class="ms-2">Carregando dados...</span>
            </td>
        </tr>
    `;
    
    const tableBody = document.querySelector(`#${tableType}-pane tbody`);
    if (tableBody) {
        tableBody.innerHTML = loadingSpinner;
        
        // Simula carregamento (substitua pela sua lógica real)
        setTimeout(() => {
            location.reload(); // Por enquanto, recarrega a página
        }, 1000);
    }
}

// Utilitários
const Utils = {
    // Formatar CPF
    formatCPF: function(cpf) {
        return cpf.replace(/(\d{3})(\d{3})(\d{3})(\d{2})/, '$1.$2.$3-$4');
    },
    
    // Formatar telefone
    formatPhone: function(phone) {
        const cleaned = phone.replace(/\D/g, '');
        if (cleaned.length === 10) {
            return cleaned.replace(/(\d{2})(\d{4})(\d{4})/, '($1) $2-$3');
        } else if (cleaned.length === 11) {
            return cleaned.replace(/(\d{2})(\d{5})(\d{4})/, '($1) $2-$3');
        }
        return phone;
    },
    
    // Validar email
    isValidEmail: function(email) {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return emailRegex.test(email);
    },
    
    // Debounce para otimizar eventos
    debounce: function(func, wait) {
        let timeout;
        return function executedFunction(...args) {
            const later = () => {
                clearTimeout(timeout);
                func(...args);
            };
            clearTimeout(timeout);
            timeout = setTimeout(later, wait);
        };
    }
};

// Exporta utilitários para uso global
window.Utils = Utils;
window.showToast = showToast;
window.clearForm = clearForm;
window.refreshTable = refreshTable;

