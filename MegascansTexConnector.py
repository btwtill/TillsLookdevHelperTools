import maya.cmds as mc

sel = mc.ls(selection=True)

shaderNode = sel.pop((len(sel)) - 1)

def filter_strings(AttributeList, filterAttributes):
    filtered_strings = []
    
    for main_Attribute in AttributeList:
        for filter_string in filterAttributes:
            if filter_string in main_Attribute:
                filtered_strings.append(main_Attribute)
                break
    return filtered_strings
    
TranslucencyTextureFilter = ["Translucency" , "translucency"]
AlbedoTextureFilter = ["Albedo", "albedo", "Color", "color"]
AOTextureFilter = ["AO", "ao"]
NormalTextureFilter = ["Normal", "normal", "N_"]
OpacityTextureFilter = ["Opacity", "opacity"]
RoughnessTextureFilter = ["Roughness",  "roughness", "_R"]
MetelnessTexutreFilter = ["Metalness", "metalness", "_M"]

for i in range(len(sel)):
    
    ##TranclucencyMap
    isTranclucency = filter_strings(sel, TranslucencyTextureFilter)
    if isTranclucency:
        
        mc.connectAttr(isTranclucency[0] + ".outColor", shaderNode + ".subsurfaceColor")
        
        sel.pop(sel.index(isTranclucency[0]))
        print(sel)
    else:
        print("already connected or not found")
        
    ##Albedo Map
    isAlbedo = filter_strings(sel, AlbedoTextureFilter)
    
    if isAlbedo:
        
        ##AO Map
        isAO = filter_strings(sel, AOTextureFilter)
        
        if isAO:
            
            aoMultiply = mc.createNode('aiMultiply')
            
            mc.connectAttr(isAO[0] + ".outColor", aoMultiply + ".input2")
            mc.connectAttr(isAlbedo[0] + ".outColor", aoMultiply + ".input1")
            
            mc.connectAttr(aoMultiply + ".outColor", shaderNode + ".baseColor")
            
            sel.pop(sel.index(isAO[0]))
            print(sel)
            
        else:
            
            mc.connectAttr(isAlbedo[0] + ".outColor",shaderNode + ".baseColor")
        
        sel.pop(sel.index(isAlbedo[0]))
        print(sel)
    else:
        pass

    ##NormalMap
    isNormal = filter_strings(sel, NormalTextureFilter)
    
    if isNormal:
        
        normalShader = mc.createNode("aiNormalMap")
        
        mc.connectAttr(isNormal[0] + ".outColor", normalShader + ".input")
        mc.connectAttr(normalShader + ".outValue", shaderNode + ".normalCamera")
        
        sel.pop(sel.index(isNormal[0]))
        print(sel)
    else:
        pass
        
    ##OpacityMap
    isOpacity = filter_strings(sel, OpacityTextureFilter)
    
    if isOpacity:
        
        mc.connectAttr(isOpacity[0] + ".outColor", shaderNode + ".opacity")
        
        sel.pop(sel.index(isOpacity[0]))
        print(sel)
    else:
        print("already connected or not found")
        
    ##Roughness Map
    isRoughness = filter_strings(sel, RoughnessTextureFilter)
    
    if isRoughness:
        
        mc.connectAttr(isRoughness[0] + ".outColorR",shaderNode + ".specularRoughness")
        
        sel.pop(sel.index(isRoughness[0]))
        print(sel)
    else:
        pass
        
    ##Metalness Map
    isMetalness = filter_strings(sel, MetelnessTexutreFilter)
    
    if isMetalness:
        
        mc.connectAttr(isMetalness[0] + ".outColorR", shaderNode + ".metalness")
        
        sel.pop(sel.index(isMetalness[0]))
        print(sel)
    else:
        pass