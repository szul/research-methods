G_SYSOBJECTS = """SELECT so.id, so.NAME, ss.NAME AS [schema]
                    FROM sysobjects AS so
                        INNER JOIN sys.schemas AS ss
                            ON so.uid = ss.SCHEMA_ID
                    WHERE so.xtype = 'u'"""
