from django.core.exceptions import ValidationError


def validate_file_size(value):
    filesize= value.size
    # 2mbs to bits = 2097152 and 3mbs to bits = 3145728
    if filesize > 3145728:
        raise ValidationError("The maximum file size that can be uploaded is 3MBs")
    else:
        return value
