import re
import os
from dictor import dictor as get_property
from xmltodict import parse as parse_xml_string
from .models.definitions import PanamahLoja, PanamahCliente, PanamahProduto, PanamahVenda, PanamahVendaItem, PanamahProdutoEan


class Nfe:
    @classmethod
    def parse_xml(cls, filename):
        with open(filename, 'r') as fp:
            return parse_xml_string(fp.read())

    @classmethod
    def deserialize_loja(cls, xml):
        root = get_property(xml, 'NFe') or get_property(xml, 'nfeProc')
        return PanamahLoja(
            id=get_property(root, 'NFe.infNFe.emit.CNPJ'),
            descricao=get_property(root, 'NFe.infNFe.emit.xNome'),
            numero_documento=get_property(root, 'NFe.infNFe.emit.CNPJ'),
            logradouro=get_property(root, 'NFe.infNFe.emit.enderEmit.xLgr'),
            numero=get_property(root, 'NFe.infNFe.emit.enderEmit.nro'),
            uf=get_property(root, 'NFe.infNFe.emit.enderEmit.UF'),
            cidade=get_property(root, 'NFe.infNFe.emit.enderEmit.xMun'),
            bairro=get_property(root, 'NFe.infNFe.emit.enderEmit.xBairro'),
            cep=get_property(root, 'NFe.infNFe.emit.enderEmit.CEP'),
            complemento=get_property(root, 'NFe.infNFe.emit.enderEmit.xCpl'),
            ativa=True,
            matriz=False,
        )

    @classmethod
    def deserialize_cliente(cls, xml):
        root = get_property(xml, 'NFe') or get_property(xml, 'nfeProc')
        return PanamahCliente(
            id=get_property(root, 'NFe.infNFe.dest.CNPJ') or get_property(root, 'NFe.infNFe.dest.CPF'),
            nome=get_property(root, 'NFe.infNFe.dest.xNome'),
            numero_documento=get_property(root, 'NFe.infNFe.dest.CNPJ') or get_property(root, 'NFe.infNFe.dest.CPF'),
            uf=get_property(root, 'NFe.infNFe.dest.enderDest.UF'),
            cidade=get_property(root, 'NFe.infNFe.dest.enderDest.xMun'),
            bairro=get_property(root, 'NFe.infNFe.dest.enderDest.xBairro'),
        )

    @classmethod
    def deserialize_produto(cls, xml):
        root = get_property(xml, 'NFe') or get_property(xml, 'nfeProc')
        dets = get_property(root, 'NFe.infNFe.det')
        dets = dets if isinstance(dets, list) else [dets]
        def get_model(det):
            produto = PanamahProduto(
                id=get_property(det, 'prod.cProd'),
                descricao=get_property(det, 'prod.xProd'),
                ativo=True
            )
            ean_tributado = get_property(det, 'prod.cEANTrib')
            ean = get_property(det, 'prod.cEAN')
            valid_ean = lambda val: val and val != 'SEM GTIN'
            if valid_ean(ean_tributado) or valid_ean(ean):
                produto.eans = []
                if ean_tributado:
                    produto.eans.append(PanamahProdutoEan(id=ean_tributado, tributado=True))
                if ean and ean != ean_tributado:
                    produto.eans.append(PanamahProdutoEan(id=ean, tributado=False))
            return produto
        return [get_model(det) for det in dets]

    @classmethod
    def deserialize_venda(cls, xml):
        root = get_property(xml, 'NFe') or get_property(xml, 'nfeProc')
        dets = get_property(root, 'NFe.infNFe.det')
        dets = dets if isinstance(dets, list) else [dets]
        return PanamahVenda(
            id=get_property(root, 'NFe.infNFe.@Id'),
            loja_id=get_property(root, 'NFe.infNFe.emit.CNPJ'),
            cliente_id=get_property(root, 'NFe.infNFe.dest.CNPJ') or get_property(
                root, 'NFe.infNFe.dest.CPF'),
            data=get_property(root, 'NFe.infNFe.ide.dhEmi'),
            data_hora_venda=get_property(root, 'NFe.infNFe.ide.dhEmi'),
            efetiva=True,
            quantidade_itens=len(dets) or 0,
            valor=get_property(root, 'NFe.infNFe.total.ICMSTot.vNF'),
            itens=[PanamahVendaItem(
                produto_id=get_property(det, 'prod.cProd'),
                quantidade=get_property(det, 'prod.qCom'),
                preco=get_property(det, 'prod.vUnCom'),
                valor_unitario=get_property(det, 'prod.vUnCom'),
                valor_total=get_property(det, 'prod.vProd'),
                desconto=get_property(det, 'prod.vDesc'),
                efetivo=True
            ) for det in dets]
        )

    @classmethod
    def read_models_from_file(cls, filename):
        basename = os.path.basename(filename)
        if not basename.startswith('ID'):
            xml = cls.parse_xml(filename)
            return [
                cls.deserialize_loja(xml),
                cls.deserialize_cliente(xml),
                cls.deserialize_venda(xml),
                *cls.deserialize_produto(xml)
            ]
        return []

    @classmethod
    def read_models_from_directory(cls, dirname):
        files = ['%s/%s' % (dirname, file) for file in os.listdir(dirname) if file.endswith('.xml')]
        has_cancel_file = lambda model: next((file for file in files if os.path.basename(file).startswith('ID110111') and re.sub(r'[^0-9]+', '', model.id) in file), False)
        model_list_by_file = [cls.read_models_from_file(file) for file in files]
        models = [model for model_list in model_list_by_file for model in model_list]
        for model in models:
            if isinstance(model, PanamahVenda) and has_cancel_file(model):
                model.efetiva = False
        return models