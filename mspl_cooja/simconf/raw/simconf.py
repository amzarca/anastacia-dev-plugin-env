# ./raw/simconf.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:e92452c8d3e28a9e27abfc9994d2007779e7f4c9
# Generated 2017-10-21 10:30:25.864635 by PyXB version 1.2.6 using Python 2.7.3.final.0
# Namespace AbsentNamespace0

from __future__ import unicode_literals
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys
import pyxb.utils.six as _six
# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:1666ca98-b63a-11e7-bc6c-08002722823d')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.6'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# A holder for module-level binding classes so we can access them from
# inside class definitions where property names may conflict.
_module_typeBindings = pyxb.utils.utility.Object()

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.CreateAbsentNamespace()
Namespace.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement, default_namespace=default_namespace)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, _six.text_type):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Complex type projectType with content type SIMPLE
class projectType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type projectType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'projectType')
    _XSDLocation = pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 3, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute EXPORT uses Python identifier EXPORT
    __EXPORT = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'EXPORT'), 'EXPORT', '__AbsentNamespace0_projectType_EXPORT', pyxb.binding.datatypes.string)
    __EXPORT._DeclarationLocation = pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 6, 8)
    __EXPORT._UseLocation = pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 6, 8)
    
    EXPORT = property(__EXPORT.value, __EXPORT.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __EXPORT.name() : __EXPORT
    })
_module_typeBindings.projectType = projectType
Namespace.addCategoryObject('typeBinding', 'projectType', projectType)


# Complex type radiomediumType with content type MIXED
class radiomediumType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type radiomediumType with content type MIXED"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'radiomediumType')
    _XSDLocation = pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 10, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element transmitting_range uses Python identifier transmitting_range
    __transmitting_range = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'transmitting_range'), 'transmitting_range', '__AbsentNamespace0_radiomediumType_transmitting_range', False, pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 12, 6), )

    
    transmitting_range = property(__transmitting_range.value, __transmitting_range.set, None, None)

    
    # Element interference_range uses Python identifier interference_range
    __interference_range = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'interference_range'), 'interference_range', '__AbsentNamespace0_radiomediumType_interference_range', False, pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 13, 6), )

    
    interference_range = property(__interference_range.value, __interference_range.set, None, None)

    
    # Element success_ratio_tx uses Python identifier success_ratio_tx
    __success_ratio_tx = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'success_ratio_tx'), 'success_ratio_tx', '__AbsentNamespace0_radiomediumType_success_ratio_tx', False, pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 14, 6), )

    
    success_ratio_tx = property(__success_ratio_tx.value, __success_ratio_tx.set, None, None)

    
    # Element success_ratio_rx uses Python identifier success_ratio_rx
    __success_ratio_rx = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'success_ratio_rx'), 'success_ratio_rx', '__AbsentNamespace0_radiomediumType_success_ratio_rx', False, pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 15, 6), )

    
    success_ratio_rx = property(__success_ratio_rx.value, __success_ratio_rx.set, None, None)

    _ElementMap.update({
        __transmitting_range.name() : __transmitting_range,
        __interference_range.name() : __interference_range,
        __success_ratio_tx.name() : __success_ratio_tx,
        __success_ratio_rx.name() : __success_ratio_rx
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.radiomediumType = radiomediumType
Namespace.addCategoryObject('typeBinding', 'radiomediumType', radiomediumType)


# Complex type eventsType with content type ELEMENT_ONLY
class eventsType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type eventsType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'eventsType')
    _XSDLocation = pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 18, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element logoutput uses Python identifier logoutput
    __logoutput = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'logoutput'), 'logoutput', '__AbsentNamespace0_eventsType_logoutput', False, pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 20, 6), )

    
    logoutput = property(__logoutput.value, __logoutput.set, None, None)

    _ElementMap.update({
        __logoutput.name() : __logoutput
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.eventsType = eventsType
Namespace.addCategoryObject('typeBinding', 'eventsType', eventsType)


# Complex type sourceType with content type SIMPLE
class sourceType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type sourceType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'sourceType')
    _XSDLocation = pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 23, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute EXPORT uses Python identifier EXPORT
    __EXPORT = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'EXPORT'), 'EXPORT', '__AbsentNamespace0_sourceType_EXPORT', pyxb.binding.datatypes.string)
    __EXPORT._DeclarationLocation = pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 26, 8)
    __EXPORT._UseLocation = pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 26, 8)
    
    EXPORT = property(__EXPORT.value, __EXPORT.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __EXPORT.name() : __EXPORT
    })
_module_typeBindings.sourceType = sourceType
Namespace.addCategoryObject('typeBinding', 'sourceType', sourceType)


# Complex type commandsType with content type SIMPLE
class commandsType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type commandsType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'commandsType')
    _XSDLocation = pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 30, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute EXPORT uses Python identifier EXPORT
    __EXPORT = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'EXPORT'), 'EXPORT', '__AbsentNamespace0_commandsType_EXPORT', pyxb.binding.datatypes.string)
    __EXPORT._DeclarationLocation = pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 33, 8)
    __EXPORT._UseLocation = pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 33, 8)
    
    EXPORT = property(__EXPORT.value, __EXPORT.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __EXPORT.name() : __EXPORT
    })
_module_typeBindings.commandsType = commandsType
Namespace.addCategoryObject('typeBinding', 'commandsType', commandsType)


# Complex type firmwareType with content type SIMPLE
class firmwareType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type firmwareType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'firmwareType')
    _XSDLocation = pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 37, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute EXPORT uses Python identifier EXPORT
    __EXPORT = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'EXPORT'), 'EXPORT', '__AbsentNamespace0_firmwareType_EXPORT', pyxb.binding.datatypes.string)
    __EXPORT._DeclarationLocation = pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 40, 8)
    __EXPORT._UseLocation = pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 40, 8)
    
    EXPORT = property(__EXPORT.value, __EXPORT.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __EXPORT.name() : __EXPORT
    })
_module_typeBindings.firmwareType = firmwareType
Namespace.addCategoryObject('typeBinding', 'firmwareType', firmwareType)


# Complex type motetypeType with content type MIXED
class motetypeType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type motetypeType with content type MIXED"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'motetypeType')
    _XSDLocation = pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 44, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element identifier uses Python identifier identifier
    __identifier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'identifier'), 'identifier', '__AbsentNamespace0_motetypeType_identifier', False, pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 46, 6), )

    
    identifier = property(__identifier.value, __identifier.set, None, None)

    
    # Element description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'description'), 'description', '__AbsentNamespace0_motetypeType_description', False, pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 47, 6), )

    
    description = property(__description.value, __description.set, None, None)

    
    # Element source uses Python identifier source
    __source = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'source'), 'source', '__AbsentNamespace0_motetypeType_source', False, pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 48, 6), )

    
    source = property(__source.value, __source.set, None, None)

    
    # Element commands uses Python identifier commands
    __commands = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'commands'), 'commands', '__AbsentNamespace0_motetypeType_commands', False, pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 49, 6), )

    
    commands = property(__commands.value, __commands.set, None, None)

    
    # Element firmware uses Python identifier firmware
    __firmware = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'firmware'), 'firmware', '__AbsentNamespace0_motetypeType_firmware', False, pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 50, 6), )

    
    firmware = property(__firmware.value, __firmware.set, None, None)

    
    # Element moteinterface uses Python identifier moteinterface
    __moteinterface = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'moteinterface'), 'moteinterface', '__AbsentNamespace0_motetypeType_moteinterface', True, pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 51, 6), )

    
    moteinterface = property(__moteinterface.value, __moteinterface.set, None, None)

    _ElementMap.update({
        __identifier.name() : __identifier,
        __description.name() : __description,
        __source.name() : __source,
        __commands.name() : __commands,
        __firmware.name() : __firmware,
        __moteinterface.name() : __moteinterface
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.motetypeType = motetypeType
Namespace.addCategoryObject('typeBinding', 'motetypeType', motetypeType)


# Complex type interface_configType with content type MIXED
class interface_configType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type interface_configType with content type MIXED"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'interface_configType')
    _XSDLocation = pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 54, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element x uses Python identifier x
    __x = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'x'), 'x', '__AbsentNamespace0_interface_configType_x', False, pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 56, 6), )

    
    x = property(__x.value, __x.set, None, None)

    
    # Element y uses Python identifier y
    __y = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'y'), 'y', '__AbsentNamespace0_interface_configType_y', False, pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 57, 6), )

    
    y = property(__y.value, __y.set, None, None)

    
    # Element z uses Python identifier z
    __z = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'z'), 'z', '__AbsentNamespace0_interface_configType_z', False, pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 58, 6), )

    
    z = property(__z.value, __z.set, None, None)

    
    # Element deviation uses Python identifier deviation
    __deviation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'deviation'), 'deviation', '__AbsentNamespace0_interface_configType_deviation', False, pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 59, 6), )

    
    deviation = property(__deviation.value, __deviation.set, None, None)

    
    # Element id uses Python identifier id
    __id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__AbsentNamespace0_interface_configType_id', False, pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 60, 6), )

    
    id = property(__id.value, __id.set, None, None)

    _ElementMap.update({
        __x.name() : __x,
        __y.name() : __y,
        __z.name() : __z,
        __deviation.name() : __deviation,
        __id.name() : __id
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.interface_configType = interface_configType
Namespace.addCategoryObject('typeBinding', 'interface_configType', interface_configType)


# Complex type moteType with content type ELEMENT_ONLY
class moteType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type moteType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'moteType')
    _XSDLocation = pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 63, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element breakpoints uses Python identifier breakpoints
    __breakpoints = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'breakpoints'), 'breakpoints', '__AbsentNamespace0_moteType_breakpoints', False, pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 65, 6), )

    
    breakpoints = property(__breakpoints.value, __breakpoints.set, None, None)

    
    # Element interface_config uses Python identifier interface_config
    __interface_config = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'interface_config'), 'interface_config', '__AbsentNamespace0_moteType_interface_config', True, pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 66, 6), )

    
    interface_config = property(__interface_config.value, __interface_config.set, None, None)

    
    # Element motetype_identifier uses Python identifier motetype_identifier
    __motetype_identifier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'motetype_identifier'), 'motetype_identifier', '__AbsentNamespace0_moteType_motetype_identifier', False, pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 67, 6), )

    
    motetype_identifier = property(__motetype_identifier.value, __motetype_identifier.set, None, None)

    _ElementMap.update({
        __breakpoints.name() : __breakpoints,
        __interface_config.name() : __interface_config,
        __motetype_identifier.name() : __motetype_identifier
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.moteType = moteType
Namespace.addCategoryObject('typeBinding', 'moteType', moteType)


# Complex type simulationType with content type ELEMENT_ONLY
class simulationType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type simulationType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'simulationType')
    _XSDLocation = pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 70, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element title uses Python identifier title
    __title = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'title'), 'title', '__AbsentNamespace0_simulationType_title', False, pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 72, 6), )

    
    title = property(__title.value, __title.set, None, None)

    
    # Element randomseed uses Python identifier randomseed
    __randomseed = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'randomseed'), 'randomseed', '__AbsentNamespace0_simulationType_randomseed', False, pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 73, 6), )

    
    randomseed = property(__randomseed.value, __randomseed.set, None, None)

    
    # Element motedelay_us uses Python identifier motedelay_us
    __motedelay_us = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'motedelay_us'), 'motedelay_us', '__AbsentNamespace0_simulationType_motedelay_us', False, pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 74, 6), )

    
    motedelay_us = property(__motedelay_us.value, __motedelay_us.set, None, None)

    
    # Element radiomedium uses Python identifier radiomedium
    __radiomedium = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'radiomedium'), 'radiomedium', '__AbsentNamespace0_simulationType_radiomedium', False, pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 75, 6), )

    
    radiomedium = property(__radiomedium.value, __radiomedium.set, None, None)

    
    # Element events uses Python identifier events
    __events = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'events'), 'events', '__AbsentNamespace0_simulationType_events', False, pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 76, 6), )

    
    events = property(__events.value, __events.set, None, None)

    
    # Element motetype uses Python identifier motetype
    __motetype = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'motetype'), 'motetype', '__AbsentNamespace0_simulationType_motetype', True, pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 77, 6), )

    
    motetype = property(__motetype.value, __motetype.set, None, None)

    
    # Element mote uses Python identifier mote
    __mote = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'mote'), 'mote', '__AbsentNamespace0_simulationType_mote', True, pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 78, 6), )

    
    mote = property(__mote.value, __mote.set, None, None)

    _ElementMap.update({
        __title.name() : __title,
        __randomseed.name() : __randomseed,
        __motedelay_us.name() : __motedelay_us,
        __radiomedium.name() : __radiomedium,
        __events.name() : __events,
        __motetype.name() : __motetype,
        __mote.name() : __mote
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.simulationType = simulationType
Namespace.addCategoryObject('typeBinding', 'simulationType', simulationType)


# Complex type pluginType with content type MIXED
class pluginType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type pluginType with content type MIXED"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'pluginType')
    _XSDLocation = pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 81, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element mote_arg uses Python identifier mote_arg
    __mote_arg = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'mote_arg'), 'mote_arg', '__AbsentNamespace0_pluginType_mote_arg', False, pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 83, 6), )

    
    mote_arg = property(__mote_arg.value, __mote_arg.set, None, None)

    
    # Element plugin_config uses Python identifier plugin_config
    __plugin_config = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'plugin_config'), 'plugin_config', '__AbsentNamespace0_pluginType_plugin_config', False, pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 84, 6), )

    
    plugin_config = property(__plugin_config.value, __plugin_config.set, None, None)

    
    # Element width uses Python identifier width
    __width = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'width'), 'width', '__AbsentNamespace0_pluginType_width', False, pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 85, 6), )

    
    width = property(__width.value, __width.set, None, None)

    
    # Element z uses Python identifier z
    __z = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'z'), 'z', '__AbsentNamespace0_pluginType_z', False, pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 86, 6), )

    
    z = property(__z.value, __z.set, None, None)

    
    # Element height uses Python identifier height
    __height = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'height'), 'height', '__AbsentNamespace0_pluginType_height', False, pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 87, 6), )

    
    height = property(__height.value, __height.set, None, None)

    
    # Element location_x uses Python identifier location_x
    __location_x = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'location_x'), 'location_x', '__AbsentNamespace0_pluginType_location_x', False, pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 88, 6), )

    
    location_x = property(__location_x.value, __location_x.set, None, None)

    
    # Element location_y uses Python identifier location_y
    __location_y = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'location_y'), 'location_y', '__AbsentNamespace0_pluginType_location_y', False, pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 89, 6), )

    
    location_y = property(__location_y.value, __location_y.set, None, None)

    _ElementMap.update({
        __mote_arg.name() : __mote_arg,
        __plugin_config.name() : __plugin_config,
        __width.name() : __width,
        __z.name() : __z,
        __height.name() : __height,
        __location_x.name() : __location_x,
        __location_y.name() : __location_y
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.pluginType = pluginType
Namespace.addCategoryObject('typeBinding', 'pluginType', pluginType)


# Complex type plugin_configType with content type ELEMENT_ONLY
class plugin_configType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type plugin_configType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'plugin_configType')
    _XSDLocation = pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 92, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element moterelations uses Python identifier moterelations
    __moterelations = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'moterelations'), 'moterelations', '__AbsentNamespace0_plugin_configType_moterelations', False, pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 94, 6), )

    
    moterelations = property(__moterelations.value, __moterelations.set, None, None)

    
    # Element skin uses Python identifier skin
    __skin = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'skin'), 'skin', '__AbsentNamespace0_plugin_configType_skin', True, pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 95, 6), )

    
    skin = property(__skin.value, __skin.set, None, None)

    
    # Element viewport uses Python identifier viewport
    __viewport = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'viewport'), 'viewport', '__AbsentNamespace0_plugin_configType_viewport', False, pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 96, 6), )

    
    viewport = property(__viewport.value, __viewport.set, None, None)

    
    # Element filter uses Python identifier filter
    __filter = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'filter'), 'filter', '__AbsentNamespace0_plugin_configType_filter', False, pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 97, 6), )

    
    filter = property(__filter.value, __filter.set, None, None)

    
    # Element formatted_time uses Python identifier formatted_time
    __formatted_time = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'formatted_time'), 'formatted_time', '__AbsentNamespace0_plugin_configType_formatted_time', False, pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 98, 6), )

    
    formatted_time = property(__formatted_time.value, __formatted_time.set, None, None)

    
    # Element coloring uses Python identifier coloring
    __coloring = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'coloring'), 'coloring', '__AbsentNamespace0_plugin_configType_coloring', False, pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 99, 6), )

    
    coloring = property(__coloring.value, __coloring.set, None, None)

    
    # Element mote uses Python identifier mote
    __mote = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'mote'), 'mote', '__AbsentNamespace0_plugin_configType_mote', True, pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 100, 6), )

    
    mote = property(__mote.value, __mote.set, None, None)

    
    # Element showRadioRXTX uses Python identifier showRadioRXTX
    __showRadioRXTX = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'showRadioRXTX'), 'showRadioRXTX', '__AbsentNamespace0_plugin_configType_showRadioRXTX', False, pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 101, 6), )

    
    showRadioRXTX = property(__showRadioRXTX.value, __showRadioRXTX.set, None, None)

    
    # Element showRadioHW uses Python identifier showRadioHW
    __showRadioHW = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'showRadioHW'), 'showRadioHW', '__AbsentNamespace0_plugin_configType_showRadioHW', False, pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 102, 6), )

    
    showRadioHW = property(__showRadioHW.value, __showRadioHW.set, None, None)

    
    # Element showLEDs uses Python identifier showLEDs
    __showLEDs = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'showLEDs'), 'showLEDs', '__AbsentNamespace0_plugin_configType_showLEDs', False, pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 103, 6), )

    
    showLEDs = property(__showLEDs.value, __showLEDs.set, None, None)

    
    # Element zoomfactor uses Python identifier zoomfactor
    __zoomfactor = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'zoomfactor'), 'zoomfactor', '__AbsentNamespace0_plugin_configType_zoomfactor', False, pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 104, 6), )

    
    zoomfactor = property(__zoomfactor.value, __zoomfactor.set, None, None)

    
    # Element notes uses Python identifier notes
    __notes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'notes'), 'notes', '__AbsentNamespace0_plugin_configType_notes', False, pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 105, 6), )

    
    notes = property(__notes.value, __notes.set, None, None)

    
    # Element decorations uses Python identifier decorations
    __decorations = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'decorations'), 'decorations', '__AbsentNamespace0_plugin_configType_decorations', False, pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 106, 6), )

    
    decorations = property(__decorations.value, __decorations.set, None, None)

    
    # Element port uses Python identifier port
    __port = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'port'), 'port', '__AbsentNamespace0_plugin_configType_port', False, pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 107, 6), )

    
    port = property(__port.value, __port.set, None, None)

    
    # Element bound uses Python identifier bound
    __bound = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'bound'), 'bound', '__AbsentNamespace0_plugin_configType_bound', False, pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 108, 6), )

    
    bound = property(__bound.value, __bound.set, None, None)

    
    # Element script uses Python identifier script
    __script = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'script'), 'script', '__AbsentNamespace0_plugin_configType_script', False, pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 109, 6), )

    
    script = property(__script.value, __script.set, None, None)

    
    # Element active uses Python identifier active
    __active = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'active'), 'active', '__AbsentNamespace0_plugin_configType_active', False, pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 110, 6), )

    
    active = property(__active.value, __active.set, None, None)

    _ElementMap.update({
        __moterelations.name() : __moterelations,
        __skin.name() : __skin,
        __viewport.name() : __viewport,
        __filter.name() : __filter,
        __formatted_time.name() : __formatted_time,
        __coloring.name() : __coloring,
        __mote.name() : __mote,
        __showRadioRXTX.name() : __showRadioRXTX,
        __showRadioHW.name() : __showRadioHW,
        __showLEDs.name() : __showLEDs,
        __zoomfactor.name() : __zoomfactor,
        __notes.name() : __notes,
        __decorations.name() : __decorations,
        __port.name() : __port,
        __bound.name() : __bound,
        __script.name() : __script,
        __active.name() : __active
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.plugin_configType = plugin_configType
Namespace.addCategoryObject('typeBinding', 'plugin_configType', plugin_configType)


# Complex type simconfType with content type ELEMENT_ONLY
class simconfType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type simconfType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'simconfType')
    _XSDLocation = pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 113, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element project uses Python identifier project
    __project = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'project'), 'project', '__AbsentNamespace0_simconfType_project', True, pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 115, 6), )

    
    project = property(__project.value, __project.set, None, None)

    
    # Element simulation uses Python identifier simulation
    __simulation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'simulation'), 'simulation', '__AbsentNamespace0_simconfType_simulation', False, pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 116, 6), )

    
    simulation = property(__simulation.value, __simulation.set, None, None)

    
    # Element plugin uses Python identifier plugin
    __plugin = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'plugin'), 'plugin', '__AbsentNamespace0_simconfType_plugin', True, pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 117, 6), )

    
    plugin = property(__plugin.value, __plugin.set, None, None)

    _ElementMap.update({
        __project.name() : __project,
        __simulation.name() : __simulation,
        __plugin.name() : __plugin
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.simconfType = simconfType
Namespace.addCategoryObject('typeBinding', 'simconfType', simconfType)


simconf = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'simconf'), simconfType, location=pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 2, 2))
Namespace.addCategoryObject('elementBinding', simconf.name().localName(), simconf)



radiomediumType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'transmitting_range'), pyxb.binding.datatypes.float, scope=radiomediumType, location=pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 12, 6)))

radiomediumType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'interference_range'), pyxb.binding.datatypes.float, scope=radiomediumType, location=pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 13, 6)))

radiomediumType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'success_ratio_tx'), pyxb.binding.datatypes.float, scope=radiomediumType, location=pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 14, 6)))

radiomediumType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'success_ratio_rx'), pyxb.binding.datatypes.float, scope=radiomediumType, location=pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 15, 6)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(radiomediumType._UseForTag(pyxb.namespace.ExpandedName(None, 'transmitting_range')), pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 12, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(radiomediumType._UseForTag(pyxb.namespace.ExpandedName(None, 'interference_range')), pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 13, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(radiomediumType._UseForTag(pyxb.namespace.ExpandedName(None, 'success_ratio_tx')), pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 14, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(radiomediumType._UseForTag(pyxb.namespace.ExpandedName(None, 'success_ratio_rx')), pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 15, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
radiomediumType._Automaton = _BuildAutomaton()




eventsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'logoutput'), pyxb.binding.datatypes.int, scope=eventsType, location=pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 20, 6)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(eventsType._UseForTag(pyxb.namespace.ExpandedName(None, 'logoutput')), pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 20, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
eventsType._Automaton = _BuildAutomaton_()




motetypeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'identifier'), pyxb.binding.datatypes.string, scope=motetypeType, location=pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 46, 6)))

motetypeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'description'), pyxb.binding.datatypes.string, scope=motetypeType, location=pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 47, 6)))

motetypeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'source'), sourceType, scope=motetypeType, location=pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 48, 6)))

motetypeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'commands'), commandsType, scope=motetypeType, location=pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 49, 6)))

motetypeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'firmware'), firmwareType, scope=motetypeType, location=pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 50, 6)))

motetypeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'moteinterface'), pyxb.binding.datatypes.string, scope=motetypeType, location=pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 51, 6)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 51, 6))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(motetypeType._UseForTag(pyxb.namespace.ExpandedName(None, 'identifier')), pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 46, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(motetypeType._UseForTag(pyxb.namespace.ExpandedName(None, 'description')), pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 47, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(motetypeType._UseForTag(pyxb.namespace.ExpandedName(None, 'source')), pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 48, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(motetypeType._UseForTag(pyxb.namespace.ExpandedName(None, 'commands')), pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 49, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(motetypeType._UseForTag(pyxb.namespace.ExpandedName(None, 'firmware')), pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 50, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(motetypeType._UseForTag(pyxb.namespace.ExpandedName(None, 'moteinterface')), pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 51, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
motetypeType._Automaton = _BuildAutomaton_2()




interface_configType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'x'), pyxb.binding.datatypes.float, scope=interface_configType, location=pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 56, 6)))

interface_configType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'y'), pyxb.binding.datatypes.float, scope=interface_configType, location=pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 57, 6)))

interface_configType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'z'), pyxb.binding.datatypes.float, scope=interface_configType, location=pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 58, 6)))

interface_configType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'deviation'), pyxb.binding.datatypes.float, scope=interface_configType, location=pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 59, 6)))

interface_configType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'id'), pyxb.binding.datatypes.byte, scope=interface_configType, location=pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 60, 6)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 56, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 57, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 58, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 59, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 60, 6))
    counters.add(cc_4)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(interface_configType._UseForTag(pyxb.namespace.ExpandedName(None, 'x')), pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 56, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(interface_configType._UseForTag(pyxb.namespace.ExpandedName(None, 'y')), pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 57, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(interface_configType._UseForTag(pyxb.namespace.ExpandedName(None, 'z')), pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 58, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(interface_configType._UseForTag(pyxb.namespace.ExpandedName(None, 'deviation')), pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 59, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(interface_configType._UseForTag(pyxb.namespace.ExpandedName(None, 'id')), pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 60, 6))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
interface_configType._Automaton = _BuildAutomaton_3()




moteType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'breakpoints'), pyxb.binding.datatypes.string, scope=moteType, location=pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 65, 6)))

moteType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'interface_config'), interface_configType, scope=moteType, location=pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 66, 6)))

moteType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'motetype_identifier'), pyxb.binding.datatypes.string, scope=moteType, location=pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 67, 6)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 66, 6))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(moteType._UseForTag(pyxb.namespace.ExpandedName(None, 'breakpoints')), pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 65, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(moteType._UseForTag(pyxb.namespace.ExpandedName(None, 'interface_config')), pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 66, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(moteType._UseForTag(pyxb.namespace.ExpandedName(None, 'motetype_identifier')), pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 67, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
moteType._Automaton = _BuildAutomaton_4()




simulationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'title'), pyxb.binding.datatypes.string, scope=simulationType, location=pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 72, 6)))

simulationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'randomseed'), pyxb.binding.datatypes.int, scope=simulationType, location=pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 73, 6)))

simulationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'motedelay_us'), pyxb.binding.datatypes.int, scope=simulationType, location=pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 74, 6)))

simulationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'radiomedium'), radiomediumType, scope=simulationType, location=pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 75, 6)))

simulationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'events'), eventsType, scope=simulationType, location=pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 76, 6)))

simulationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'motetype'), motetypeType, scope=simulationType, location=pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 77, 6)))

simulationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'mote'), moteType, scope=simulationType, location=pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 78, 6)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 77, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 78, 6))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(simulationType._UseForTag(pyxb.namespace.ExpandedName(None, 'title')), pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 72, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(simulationType._UseForTag(pyxb.namespace.ExpandedName(None, 'randomseed')), pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 73, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(simulationType._UseForTag(pyxb.namespace.ExpandedName(None, 'motedelay_us')), pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 74, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(simulationType._UseForTag(pyxb.namespace.ExpandedName(None, 'radiomedium')), pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 75, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(simulationType._UseForTag(pyxb.namespace.ExpandedName(None, 'events')), pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 76, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(simulationType._UseForTag(pyxb.namespace.ExpandedName(None, 'motetype')), pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 77, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(simulationType._UseForTag(pyxb.namespace.ExpandedName(None, 'mote')), pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 78, 6))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
simulationType._Automaton = _BuildAutomaton_5()




pluginType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'mote_arg'), pyxb.binding.datatypes.byte, scope=pluginType, location=pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 83, 6)))

pluginType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'plugin_config'), plugin_configType, scope=pluginType, location=pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 84, 6)))

pluginType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'width'), pyxb.binding.datatypes.short, scope=pluginType, location=pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 85, 6)))

pluginType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'z'), pyxb.binding.datatypes.byte, scope=pluginType, location=pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 86, 6)))

pluginType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'height'), pyxb.binding.datatypes.short, scope=pluginType, location=pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 87, 6)))

pluginType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'location_x'), pyxb.binding.datatypes.short, scope=pluginType, location=pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 88, 6)))

pluginType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'location_y'), pyxb.binding.datatypes.short, scope=pluginType, location=pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 89, 6)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 83, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 84, 6))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(pluginType._UseForTag(pyxb.namespace.ExpandedName(None, 'mote_arg')), pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 83, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(pluginType._UseForTag(pyxb.namespace.ExpandedName(None, 'plugin_config')), pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 84, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(pluginType._UseForTag(pyxb.namespace.ExpandedName(None, 'width')), pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 85, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(pluginType._UseForTag(pyxb.namespace.ExpandedName(None, 'z')), pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 86, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(pluginType._UseForTag(pyxb.namespace.ExpandedName(None, 'height')), pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 87, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(pluginType._UseForTag(pyxb.namespace.ExpandedName(None, 'location_x')), pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 88, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(pluginType._UseForTag(pyxb.namespace.ExpandedName(None, 'location_y')), pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 89, 6))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
pluginType._Automaton = _BuildAutomaton_6()




plugin_configType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'moterelations'), pyxb.binding.datatypes.string, scope=plugin_configType, location=pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 94, 6)))

plugin_configType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'skin'), pyxb.binding.datatypes.string, scope=plugin_configType, location=pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 95, 6)))

plugin_configType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'viewport'), pyxb.binding.datatypes.string, scope=plugin_configType, location=pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 96, 6)))

plugin_configType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'filter'), pyxb.binding.datatypes.string, scope=plugin_configType, location=pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 97, 6)))

plugin_configType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'formatted_time'), pyxb.binding.datatypes.string, scope=plugin_configType, location=pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 98, 6)))

plugin_configType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'coloring'), pyxb.binding.datatypes.string, scope=plugin_configType, location=pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 99, 6)))

plugin_configType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'mote'), pyxb.binding.datatypes.byte, scope=plugin_configType, location=pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 100, 6)))

plugin_configType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'showRadioRXTX'), pyxb.binding.datatypes.string, scope=plugin_configType, location=pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 101, 6)))

plugin_configType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'showRadioHW'), pyxb.binding.datatypes.string, scope=plugin_configType, location=pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 102, 6)))

plugin_configType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'showLEDs'), pyxb.binding.datatypes.string, scope=plugin_configType, location=pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 103, 6)))

plugin_configType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'zoomfactor'), pyxb.binding.datatypes.float, scope=plugin_configType, location=pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 104, 6)))

plugin_configType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'notes'), pyxb.binding.datatypes.string, scope=plugin_configType, location=pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 105, 6)))

plugin_configType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'decorations'), pyxb.binding.datatypes.string, scope=plugin_configType, location=pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 106, 6)))

plugin_configType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'port'), pyxb.binding.datatypes.int, scope=plugin_configType, location=pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 107, 6)))

plugin_configType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'bound'), pyxb.binding.datatypes.string, scope=plugin_configType, location=pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 108, 6)))

plugin_configType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'script'), pyxb.binding.datatypes.string, scope=plugin_configType, location=pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 109, 6)))

plugin_configType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'active'), pyxb.binding.datatypes.string, scope=plugin_configType, location=pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 110, 6)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 94, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 95, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 96, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 97, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 98, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 99, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 100, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 101, 6))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 102, 6))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 103, 6))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 104, 6))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 105, 6))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 106, 6))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 107, 6))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 108, 6))
    counters.add(cc_14)
    cc_15 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 109, 6))
    counters.add(cc_15)
    cc_16 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 110, 6))
    counters.add(cc_16)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(plugin_configType._UseForTag(pyxb.namespace.ExpandedName(None, 'moterelations')), pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 94, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(plugin_configType._UseForTag(pyxb.namespace.ExpandedName(None, 'skin')), pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 95, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(plugin_configType._UseForTag(pyxb.namespace.ExpandedName(None, 'viewport')), pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 96, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(plugin_configType._UseForTag(pyxb.namespace.ExpandedName(None, 'filter')), pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 97, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(plugin_configType._UseForTag(pyxb.namespace.ExpandedName(None, 'formatted_time')), pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 98, 6))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(plugin_configType._UseForTag(pyxb.namespace.ExpandedName(None, 'coloring')), pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 99, 6))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(plugin_configType._UseForTag(pyxb.namespace.ExpandedName(None, 'mote')), pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 100, 6))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(plugin_configType._UseForTag(pyxb.namespace.ExpandedName(None, 'showRadioRXTX')), pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 101, 6))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(plugin_configType._UseForTag(pyxb.namespace.ExpandedName(None, 'showRadioHW')), pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 102, 6))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(plugin_configType._UseForTag(pyxb.namespace.ExpandedName(None, 'showLEDs')), pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 103, 6))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(plugin_configType._UseForTag(pyxb.namespace.ExpandedName(None, 'zoomfactor')), pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 104, 6))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(plugin_configType._UseForTag(pyxb.namespace.ExpandedName(None, 'notes')), pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 105, 6))
    st_11 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(plugin_configType._UseForTag(pyxb.namespace.ExpandedName(None, 'decorations')), pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 106, 6))
    st_12 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(plugin_configType._UseForTag(pyxb.namespace.ExpandedName(None, 'port')), pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 107, 6))
    st_13 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_14, False))
    symbol = pyxb.binding.content.ElementUse(plugin_configType._UseForTag(pyxb.namespace.ExpandedName(None, 'bound')), pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 108, 6))
    st_14 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_15, False))
    symbol = pyxb.binding.content.ElementUse(plugin_configType._UseForTag(pyxb.namespace.ExpandedName(None, 'script')), pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 109, 6))
    st_15 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_16, False))
    symbol = pyxb.binding.content.ElementUse(plugin_configType._UseForTag(pyxb.namespace.ExpandedName(None, 'active')), pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 110, 6))
    st_16 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_11, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_12, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_12, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_13, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_13, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_14, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_14, False) ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_15, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_15, False) ]))
    st_15._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_16, True) ]))
    st_16._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
plugin_configType._Automaton = _BuildAutomaton_7()




simconfType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'project'), projectType, scope=simconfType, location=pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 115, 6)))

simconfType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'simulation'), simulationType, scope=simconfType, location=pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 116, 6)))

simconfType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'plugin'), pluginType, scope=simconfType, location=pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 117, 6)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 115, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 117, 6))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(simconfType._UseForTag(pyxb.namespace.ExpandedName(None, 'project')), pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 115, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(simconfType._UseForTag(pyxb.namespace.ExpandedName(None, 'simulation')), pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 116, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(simconfType._UseForTag(pyxb.namespace.ExpandedName(None, 'plugin')), pyxb.utils.utility.Location('/home/user/venv_anastacia/iot-deployment-agent/xml_parser/simconf/simconf.xsd', 117, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
simconfType._Automaton = _BuildAutomaton_8()

