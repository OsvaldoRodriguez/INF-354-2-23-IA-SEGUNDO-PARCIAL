
DROP PROCEDURE IF EXISTS EliminarTablaNombre;

CREATE PROCEDURE EliminarTablaNombre
AS
BEGIN
    IF OBJECT_ID('nombre', 'U') IS NOT NULL
    BEGIN
        DROP TABLE nombre;
        PRINT 'La tabla ha sido eliminada.';
    END
    ELSE
    BEGIN
        PRINT 'La tabla no existe.';
    END;
END;


EXEC EliminarTablaNombre;


DROP PROCEDURE IF EXISTS GenerarTablaDesdePalabra;

CREATE PROCEDURE GenerarTablaDesdePalabra
    @palabra1 varchar(20),
    @palabra2 varchar(20)
AS
BEGIN
    DECLARE 
	@longitud1 INT, 
	@longitud2 INT, 
	@posicion INT, 
	@letra VARCHAR(2), 
	@contador INT, 
	@sql NVARCHAR(MAX), 
	@columna VARCHAR(4), 
	@contar INT,
	@palabra11 varchar(MAX),
	@palabra22 varchar(MAX);
    DECLARE @diferencias INT = 0;

    -- Eliminar la tabla si existe
    EXEC EliminarTablaNombre;

    SET @longitud1 = LEN(@palabra1);
    SET @longitud2 = LEN(@palabra2);
	set @palabra11 = @palabra1;
	SET @palabra22 = @palabra2;
    SET @posicion = 1;
    SET @sql = 'CREATE TABLE nombre (';

    -- Crear tabla con columnas
    WHILE @posicion <= @longitud1
    BEGIN
        SET @letra = LEFT(@palabra1, 1);
        SET @palabra1 = RIGHT(@palabra1, LEN(@palabra1)-1);
        SET @sql = @sql + @letra + CAST(@posicion AS VARCHAR) + ' INT, ';
        SET @posicion = @posicion + 1;
    END;

    SET @sql = LEFT(@sql, LEN(@sql)-1) + ')';
    EXEC sp_executesql @sql;

    SET @posicion = 1;

    -- Insertar datos en la tabla
    WHILE @posicion <= @longitud2
    BEGIN
        SET @letra = LEFT(@palabra2, 1);
        SET @palabra2 = RIGHT(@palabra2, LEN(@palabra2)-1);
        SET @contar = 0;

        -- Verificar si la columna ya existe
        SELECT @contar = COUNT(*)
        FROM INFORMATION_SCHEMA.COLUMNS
        WHERE TABLE_NAME = 'nombre'
          AND LEFT(COLUMN_NAME,1) = @letra
          AND ORDINAL_POSITION <= @posicion;

        IF @contar > 0
        BEGIN
            -- Obtener la primera columna que coincida
            SELECT TOP 1 @columna = COLUMN_NAME
            FROM INFORMATION_SCHEMA.COLUMNS
            WHERE TABLE_NAME = 'nombre'
              AND LEFT(COLUMN_NAME,1) = @letra
              AND ORDINAL_POSITION >= @posicion;

            -- Insertar un valor en la columna
            SET @sql = 'INSERT INTO nombre(' + @columna + ') VALUES(1)';
            EXEC sp_executesql @sql;

        END;

        SET @posicion = @posicion + 1;
    END;

    SET @sql = 'SELECT ';

    -- Construir la consulta final
    SELECT @contar = COUNT(*)
    FROM INFORMATION_SCHEMA.COLUMNS
    WHERE TABLE_NAME = 'nombre';

    SET @posicion = 1;

    WHILE @posicion <= @contar
    BEGIN
        SELECT @columna = COLUMN_NAME
        FROM INFORMATION_SCHEMA.COLUMNS
        WHERE TABLE_NAME = 'nombre' AND ORDINAL_POSITION = @posicion;

        SET @sql = @sql + 'SUM(ISNULL(' + @columna + ', 0)) + ';
        SET @posicion = @posicion + 1;
    END;

    SET @sql = LEFT(@sql, LEN(@sql)-1) + ' from nombre';

    --PRINT @sql;

    -- Ejecutar la consulta dinámica y guardar en la tabla diferencia
    --EXEC sp_executesql @sql;

    
	SET @posicion = 1;
    SET @diferencias = 0;

    -- Verificar la longitud máxima entre las dos palabras
    DECLARE @longitudMaxima INT;
    SET @longitudMaxima = CASE WHEN @longitud1 > @longitud2 THEN @longitud1 ELSE @longitud2 END;

    -- Comparar caracteres en cada posición
    WHILE @posicion <= @longitudMaxima
    BEGIN
        IF SUBSTRING(@palabra11, @posicion, 1) != SUBSTRING(@palabra22, @posicion, 1)
        BEGIN
            SET @diferencias = @diferencias + 1;
        END;

        SET @posicion = @posicion + 1;
    END;

    -- Calcular el porcentaje de diferencias
    DECLARE @porcentajeDiferencias FLOAT;
    SET @porcentajeDiferencias = (CAST(@diferencias AS FLOAT) / CAST(@longitudMaxima AS FLOAT)) * 100;

    -- Mostrar el resultado
    PRINT 'Palabra 1: ' + @palabra11;
    PRINT 'Palabra 2: ' + @palabra22;
    PRINT 'Porcentaje de Diferencias: ' + CAST(@porcentajeDiferencias AS VARCHAR) + '%';
END;


EXEC GenerarTablaDesdePalabra 'qwetryuiio', 'zxcvcvbm';


SELECT
    DB_NAME() AS CurrentDatabase,
    HOST_NAME() AS HostName,
    SUSER_NAME() AS UserName;
