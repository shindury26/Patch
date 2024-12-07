from toyecc import AffineCurvePoint, getcurvebyname, FieldElement,ECPrivateKey,ECPublicKey,Tools

def generate_eddsa_keypair():
    curve = getcurvebyname("Ed25519")   
    private_key = ECPrivateKey.eddsa_generate(curve)
    return private_key.eddsa_encode(), private_key.pubkey.eddsa_encode()

def generate_kcdsa_keypair():
    curve = getcurvebyname("Curve25519")   
    private_key = ECPrivateKey.generate(curve)
    return Tools.inttobytes_le(private_key.scalar, 32), Tools.inttobytes_le(int(private_key.pubkey.point.x), 32)

if __name__ == '__main__':
    eddsa_private_key, eddsa_public_key = generate_eddsa_keypair()
    kcdsa_private_key, kcdsa_public_key = generate_kcdsa_keypair()
    print(f'CUSTOM_NPK_SIGN_PRIVATE_KEY: {eddsa_private_key.hex().upper()}')
    print(f'CUSTOM_NPK_SIGN_PUBLIC_KEY: {eddsa_public_key.hex().upper()}')
    print(f'CUSTOM_LICENSE_PRIVATE_KEY: {kcdsa_private_key.hex().upper()}')
    print(f'CUSTOM_LICENSE_PUBLIC_KEY: {kcdsa_public_key.hex().upper()}')
    print(f'MIKRO_LICENSE_PUBLIC_KEY: 8E1067E4305FCDC0CFBF95C10F96E5DFE8C49AEF486BD1A4E2E96C27F01E3E32')  
    print(f'MIKRO_NPK_SIGN_PUBLIC_LKEY: C293CED638A2A33C681FC8DE98EE26C54EADC5390C2DFCE197D35C83C416CF59')  
    print(f'MIKRO_UPGRADE_URL: upgrade.mikrotik.com')  

    print(f'MIKRO_CLOUD_URL: upgrade.mikrotik.com')  
    print(f'MIKRO_CLOUD_PUBLIC_KEY: 8E1067E4305FCDC0CFBF95C10F96E5D1FE8C49AEF486BD1A4E2E96C27F01E3E32')  
    print(f'CUSTOM_CLOUD_URL: upgrade.mikrotik.com')  
    print(f'CUSTOM_CLOUD_PUBLIC_KEY: 8E1067E4305FCDC0CFBF95C10F96E5DFE8C49AEF486BD1A4E2E96C27F01E3E32')   
    print(f'MIKRO_RENEW_URL: upgrade.mikrotik.com')  
    print(f'CUSTOM_RENEW_URL: upgrade.mikrotik.com')  

    print(f'MIKRO_LICENCE_URL: mikrotik.com/client/keyinfo')
    print(f'CUSTOM_LICENCE_URL: mikrotik.com/client/keyinfo')
    print(f'CUSTOM_UPGRADE_URL: upgrade.mikrotik.com')
       
     


    