from .stream import PanamahStream
from .models.definitions import PanamahProduto, PanamahProdutoComposicao, PanamahProdutoComposicaoItem, PanamahProdutoFornecedor, PanamahProdutoEan
from datetime import datetime
from os import environ

#inicializando a api de streaming
stream = PanamahStream(
    authorization_token= environ.get('PANAMAH_AUTHORIZATION_TOKEN'), #(opcional) caso não seja passado, é considerado a variável de ambiente PANAMAH_AUTHORIZATION_TOKEN
    secret= environ.get('PANAMAH_SECRET'), #(opcional) caso não seja passado, é considerado a variável de ambiente PANAMAH_SECRET
)

produto = PanamahProduto(
    id= '689',
    descricao= 'Coca-cola',
    data_inclusao= datetime.now(),
    secao_id= '999',
    composicao= PanamahProdutoComposicao(
        quantidade= 2,
        itens= [
            PanamahProdutoComposicaoItem(
                produto_id= '432',
                quantidade= 1
            ),
            PanamahProdutoComposicaoItem(
                produto_id= '567',
                quantidade= 1
            )
        ]
    ),
    fornecedores= [
        PanamahProdutoFornecedor(
            id= '222',
            principal= True
        )
    ]
)

try:
    stream.save(produto, '02541926375') #salvando para o primeiro assinante
except ValueError as e: 
    print(e) #erro na validação do modelo

#sempre chamar antes de finalizar a aplicação
stream.flush()