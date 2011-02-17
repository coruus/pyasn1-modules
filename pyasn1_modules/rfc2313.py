from pyasn1.type import univ, namedtype, namedval, constraint

class DSAPrivateKey(univ.Sequence):
    """PKIX compliant DSA private key structure"""
    componentType = namedtype.NamedTypes(
        namedtype.NamedType('version', univ.Integer(namedValues=namedval.NamedValues(('v1', 0)))),
        namedtype.NamedType('p', univ.Integer()),
        namedtype.NamedType('q', univ.Integer()),
        namedtype.NamedType('g', univ.Integer()),
        namedtype.NamedType('public', univ.Integer()),
        namedtype.NamedType('private', univ.Integer())
        )

MAX = 16

class OtherPrimeInfo(univ.Sequence):
    componentType = namedtype.NamedTypes(
        namedtype.NamedType('prime', univ.Integer()),
        namedtype.NamedType('exponent', univ.Integer()),
        namedtype.NamedType('coefficient', univ.Integer())
        )
    
class OtherPrimeInfos(univ.SequenceOf):
    componentType = OtherPrimeInfo()
    subtypeSpec = univ.SequenceOf.subtypeSpec + \
                  constraint.ValueSizeConstraint(1, MAX)
    
class RSAPrivateKey(univ.Sequence):
    """PKCS#1 compliant RSA private key structure"""
    componentType = namedtype.NamedTypes(
        namedtype.NamedType('version', univ.Integer(namedValues=namedval.NamedValues(('two-prime', 0), ('multi', 1)))),
        namedtype.NamedType('modulus', univ.Integer()),
        namedtype.NamedType('publicExponent', univ.Integer()),
        namedtype.NamedType('privateExponent', univ.Integer()),
        namedtype.NamedType('prime1', univ.Integer()),
        namedtype.NamedType('prime2', univ.Integer()),
        namedtype.NamedType('exponent1', univ.Integer()),
        namedtype.NamedType('exponent2', univ.Integer()),
        namedtype.NamedType('coefficient', univ.Integer()),
        namedtype.OptionalNamedType('otherPrimeInfos', OtherPrimeInfos())
        )
    
