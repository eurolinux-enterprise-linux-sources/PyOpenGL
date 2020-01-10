'''OpenGL extension EXT.framebuffer_object

This module customises the behaviour of the 
OpenGL.raw.GL.EXT.framebuffer_object to provide a more 
Python-friendly API
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL.EXT.framebuffer_object import *
### END AUTOGENERATED SECTION

glGenFramebuffersEXT = wrapper.wrapper(glGenFramebuffersEXT).setOutput(
                'framebuffers', 
                lambda x: (x,), 
                'n')
                
glGenRenderbuffersEXT = wrapper.wrapper(glGenRenderbuffersEXT).setOutput(
                'renderbuffers', 
                lambda x: (x,), 
                'n')

#glBindRenderbufferEXT # doesn't require wrapping
#glBindFramebufferEXT  # doesn't require wrapping
#glBindRenderbufferEXT # doesn't require wrapping
#glCheckFramebufferStatusEXT
#glDeleteFramebuffersEXT # should be wrapped to eliminate 'length'
#glDeleteRenderbuffersEXT # should be wrapped to eliminate 'length'
#glFramebufferRenderbufferEXT
#glFramebufferTexture1DEXT
#glFramebufferTexture2DEXT
#glFramebufferTexture3DEXT
#glGenFramebuffersEXT  # wrapped
#glGenRenderbuffersEXT # wrapped
#glGenerateMipmapEXT
#glGetFramebufferAttachmentParameterivEXT
#glGetRenderbufferParameterivEXT
#glInitFramebufferObjectEXT
#glIsFramebufferEXT
#glIsRenderbufferEXT
#glRenderbufferStorageEXT # doesn't require wrapping                                          
#glget.addGLGetConstant( GL_MAX_COLOR_ATTACHMENTS_EXT, (1,))
#glget.addGLGetConstant( GL_FRAMEBUFFER_BINDING_EXT, (1,))
#glget.addGLGetConstant( GL_RENDERBUFFER_BINDING_EXT, (1,))
#glget.addGLGetConstant( GL_MAX_RENDERBUFFER_SIZE_EXT, (1,))
