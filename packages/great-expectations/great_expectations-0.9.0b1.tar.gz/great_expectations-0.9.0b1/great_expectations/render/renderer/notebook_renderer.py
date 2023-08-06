import os
import nbformat

from great_expectations.core import NamespaceAwareExpectationSuite
from great_expectations.render.renderer.renderer import Renderer


class NotebookRenderer(Renderer):
    """
    Render a notebook that can re-create or edit the suite.

    Possible use cases:
    - Make an easy path to edit a suite that a Profiler created.
    - Make it easy to edit a suite where only JSON exists.
    """

    @classmethod
    def _get_expectations_by_column(cls, expectations):
        # TODO probably replace this with Suite logic at some point
        expectations_by_column = {"table_expectations": []}
        for exp in expectations:
            if "_table_" in exp["expectation_type"]:
                expectations_by_column["table_expectations"].append(exp)
            else:
                col = exp["kwargs"]["column"]

                if col not in expectations_by_column.keys():
                    expectations_by_column[col] = []
                expectations_by_column[col].append(exp)
        return expectations_by_column

    @classmethod
    def _build_kwargs_string(cls, expectation):
        kwargs = []
        for k, v in expectation["kwargs"].items():
            if k == "column":
                # make the column a positional argument
                kwargs.append(f"'{v}'")
            elif isinstance(v, str):
                # Put strings in quotes
                kwargs.append(f"{k}='{v}'")
            else:
                # Pass other types as is
                kwargs.append(f"{k}={v}")

        return ", ".join(kwargs)

    def add_header(self, data_asset_name=None, suite_name=None):
        # TODO better wording in the intro cells
        self.add_markdown_cell(
            f"""# Edit the Scaffolded Expectation Suite
Use this notebook to recreate and modify your expectation suite for:
- **Data Asset**: `{data_asset_name}`
- **Expectation Suite Name**: `{suite_name}`

We'd love it if you **reach out for help on** the [**Great Expectations Slack Channel**](https://greatexpectations.io/slack)"""
        )
        self.add_code_cell(
            """\
import os
import json
from datetime import datetime
import great_expectations as ge
import great_expectations.jupyter_ux"""
        )
        self.add_markdown_cell(
            """\
## 1. Get a DataContext
This represents your **project** that you just created using `great_expectations init`. [Read more in the tutorial](https://docs.greatexpectations.io/en/latest/tutorials/create_expectations.html?utm_source=notebook&utm_medium=create_expectations#get-a-datacontext-object)"""
        )
        self.add_code_cell("context = ge.data_context.DataContext()")

        self.add_markdown_cell(
            """\
## 2. Optional: Rename your Expectation Suite

We recommend naming your first expectation suite for a table `warning`. Later, \
as you identify some of the expectations that you add to this suite as \
critical, you can move these expectations into another suite and call it \
`failure`.
""")
        self.add_code_cell(
            """\
expectation_suite_name = "{}" # TODO: replace with your value!
context.create_expectation_suite(data_asset_name="{}", expectation_suite_name=expectation_suite_name, overwrite_existing=True);""".format(suite_name, data_asset_name)
       )

    def add_footer(self):
        self.add_markdown_cell(
            """\
## Save & Review Your Expectations

Run the next cell to save the expectation suite as a JSON file in the `great_expectations/expectations` directory of your project.
If you decide not to save some expectations that you created, use [remove_expectaton method](https://docs.greatexpectations.io/en/latest/module_docs/data_asset_module.html?highlight=remove_expectation&utm_source=notebook&utm_medium=edit_expectations#great_expectations.data_asset.data_asset.DataAsset.remove_expectation).

Let's now rebuild your Data Docs, which helps you communicate about your data with both machines and humans."""
        )
        # TODO this may become confusing for users depending on what they are trying
        #  to accomplish in their dev loop
        self.add_code_cell(
            """\
batch.save_expectation_suite(discard_failed_expectations=False)

# Let's make a simple sortable timestamp. Note this could come from your pipeline runner.
run_id = datetime.utcnow().isoformat().replace(":", "") + "Z"

results = context.run_validation_operator(
    assets_to_validate=[batch],
    run_id=run_id,
    validation_operator_name="action_list_operator",
)
context.build_data_docs()
context.open_data_docs()"""
        )

    def add_batch_cells(self, data_asset_name, batch_kwargs, suite_name=None):
        """Add backend-specific batch cells.
        :param batch_kwargs:
        """
        self.add_markdown_cell(
            """\
## 3. Load a batch of data you want to use to create `Expectations`

To learn more about batches and `get_batch`, see [this tutorial](https://docs.greatexpectations.io/en/latest/tutorials/create_expectations.html?utm_source=notebook&utm_medium=create_expectations#load-a-batch-of-data-to-create-expectations)
Let's glance at a bit of your data."""
        )

        # TODO such brittle hacks to fix paths for a demo
        if "path" in batch_kwargs.keys():
            base_dir = batch_kwargs["path"]
            if not base_dir.startswith("/"):
                batch_kwargs["path"] = os.path.join("../../", base_dir)

        # TODO caution about the .head() showing data that could be committed.
        self.add_code_cell(
            """\
batch_kwargs = {}
batch = context.get_batch("{}", expectation_suite_name, batch_kwargs)
batch.head()""".format(batch_kwargs, data_asset_name)
        )

    def add_code_cell(self, code):
        """
        Add the given code as a new code cell.
        :param code:
        """
        cell = nbformat.v4.new_code_cell(code)
        self.notebook["cells"].append(cell)

    def add_markdown_cell(self, markdown):
        """
        Add the given markdown as a new markdown cell.
        :param markdown:
        """
        cell = nbformat.v4.new_markdown_cell(markdown)
        self.notebook["cells"].append(cell)

    def add_expectation_cells_from_suite(self, expectations):
        expectations_by_column = self._get_expectations_by_column(expectations)
        self.add_markdown_cell(f"### Table Expectation(s)")
        if expectations_by_column["table_expectations"]:
            for exp in expectations_by_column["table_expectations"]:
                kwargs_string = self._build_kwargs_string(exp)
                self.add_code_cell(f"batch.{exp['expectation_type']}({kwargs_string})")
        else:
            self.add_markdown_cell(
                "No table level expectations are in this suite. Feel free to add some."
            )

        # Remove the table expectations since they are dealt with
        expectations_by_column.pop("table_expectations")

        self.add_markdown_cell("### Column Expectation(s)")

        for column, expectations in expectations_by_column.items():
            self.add_markdown_cell(f"#### `{column}`")

            for exp in expectations:
                kwargs_string = self._build_kwargs_string(exp)
                self.add_code_cell(f"batch.{exp['expectation_type']}({kwargs_string})")

    @classmethod
    def _write_notebook_to_disk(cls, notebook, notebook_file_path):
        with open(notebook_file_path, "w") as f:
            nbformat.write(notebook, f)

    def render(self, suite, batch_kwargs):
        """
        Render a notebook dict from an expectation suite.
        """
        if not isinstance(suite, NamespaceAwareExpectationSuite):
            raise RuntimeWarning(
                "render must be given a NamespaceAwareExpectationSuite."
            )
        if not isinstance(batch_kwargs, dict):
            raise RuntimeWarning("render must be given a dictionary of batch_kwargs.")

        self.notebook = nbformat.v4.new_notebook()

        data_asset_name = suite.data_asset_name
        suite_name = suite.expectation_suite_name

        # Compose the notebook sections from generic + backend-specific cells
        self.add_header(data_asset_name, suite_name)
        self.add_batch_cells(data_asset_name, batch_kwargs, suite_name)
        self.add_authoring_intro()
        self.add_expectation_cells_from_suite(suite.expectations)
        self.add_footer()

        return self.notebook

    def render_to_disk(self, suite, batch_kwargs, notebook_file_path):
        """
        Render a notebook to disk from an expectation suite.

        :param batch_kwargs:
        :type suite: dict
        :type notebook_file_path: str
        """
        self.render(suite, batch_kwargs)
        self._write_notebook_to_disk(self.notebook, notebook_file_path)

    def add_authoring_intro(self):
        self.add_markdown_cell(
            """\
## 3. Create & Edit Expectations

With a batch, you can add expectations by calling specific expectation methods. They all begin with `.expect_` which makes autocompleting easy.

See available expectations in the [expectation glossary](https://docs.greatexpectations.io/en/latest/reference/expectation_glossary.html?utm_source=notebook&utm_medium=create_expectations).
You can also see available expectations by hovering over data elements in DataDocs generated by profiling your dataset. [Read more in the tutorial](https://docs.greatexpectations.io/en/latest/tutorials/create_expectations.html?utm_source=notebook&utm_medium=create_expectations#author-expectations)"""
        )


# class SQLNotebookRenderer(NotebookRenderer):
#     def add_batch_cells(self, context, data_asset_name, suite_name=None):
#         self.add_markdown_cell(
#             """\
# ## 2. Load a batch of data you want to use to create `Expectations`
#
# To learn more about batches and `get_batch`, see [this tutorial](https://docs.greatexpectations.io/en/latest/tutorials/create_expectations.html?utm_source=notebook&utm_medium=create_expectations#load-a-batch-of-data-to-create-expectations)"""
#         )
#         table_name = data_asset_name.split("/")[-1]
#         self.add_code_cell(
#             """\
# batch_kwargs = {"query": "SELECT * FROM """
#             + table_name
#             + """\"}
# batch = context.get_batch(\""""
#             + str(data_asset_name)
#             + '", "'
#             + str(suite_name)
#             + '", batch_kwargs)'
#         )
