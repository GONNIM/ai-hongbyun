style_main = """
    <style>
    .header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 0.625rem 0;
    }
    .header input {
        flex-grow: 1;
        margin: 0 1.25rem;
        padding: 0.625rem;
    }
    .header a {
        margin-left: 0.625rem;
    }
    .footer {
        text-align: center;
        padding: 0.625rem 0;
        margin-top: 1.25rem;
    }
    .law-card {
        border: 1px solid #ddd;
        border-radius: 0.5rem;
        padding: 1.25rem;
        text-align: center;
        transition: background-color 0.3s;
        margin-top: 1.25rem;
    }
    .law-icon {
        width: 3.125rem;
        height: 3.125rem;
    }
    .law-name {
        font-size: 4.125rem;
        margin: 0.625rem 0;
    }
    .law-description {
        font-size: 1.875rem;
        color: #555;
    }
    .law-link {
        display: inline-block;
        margin-top: 2.625rem;
        margin-bottom: 1.625rem;
        padding: 0.625rem 1.25rem;
        background-color: #34495e;
        color: #fff;
        text-decoration: none;
        border-radius: 0.25rem;
        transition: background-color 0.3s;
    }
    
    @media (max-width: 48rem) {
        .law-card {
            padding: 0.625rem;
        }
        .law-name {
            font-size: 1rem;
        }
        .law-description {
            font-size: 0.75rem;
        }
        .law-link {
            padding: 0.5rem 1rem;
        }
    }

    @media (max-width: 30rem) {
        .header {
            flex-direction: column;
        }
        .header input {
            margin: 0.625rem 0;
        }
        .law-card {
            padding: 0.625rem;
            margin-top: 0.625rem;
        }
        .law-name {
            font-size: 0.875rem;
        }
        .law-description {
            font-size: 0.75rem;
        }
        .law-link {
            padding: 0.5rem 1rem;
        }
    }
    </style>
"""
